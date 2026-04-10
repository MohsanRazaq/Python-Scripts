# ============================================================
# MITM Attack Simulation (Educational Purpose Only)
# ============================================================

import datetime
from cryptography.fernet import Fernet

# ---------------- ENCRYPTION SETUP ----------------
key = Fernet.generate_key()
cipher = Fernet(key)

# ---------------- LOG ----------------
interception_log = []

# ---------------- CLIENT ----------------
class Client:
    def send_message(self):
        message = {
            'sender': 'mohsan',
            'receiver': 'bank_server',
            'username': 'noni_pk',
            'password': 'SecureP@ss123',
            'action': 'fund_transfer',
            'amount': 5000,
            'to_account': 'BOB-9921'
        }
        print("[ALICE] Sending transaction...")
        return message

# ---------------- DEFENDER (ENCRYPTION) ----------------
class Defender:
    def encrypt(self, message):
        return cipher.encrypt(str(message).encode())

    def decrypt(self, encrypted_message):
        return cipher.decrypt(encrypted_message).decode()

# ---------------- ATTACKER ----------------
class Attacker:
    def intercept(self, data):
        print("\n[EVE] ===== INTERCEPTED =====")

        # If encrypted → cannot read
        if isinstance(data, bytes):
            print("[EVE] Encrypted data captured (cannot read)")
            return data

        # Log data
        timestamp = datetime.datetime.now()
        interception_log.append({'time': timestamp, 'data': dict(data)})

        for k, v in data.items():
            print(f"[EVE] {k}: {v}")

        # Modify data
        print("\n[EVE] Tampering data...")
        data['amount'] = 99999
        data['to_account'] = 'EVE-4567'

        return data

# ---------------- SERVER ----------------
class Server:
    def receive(self, data):
        print("\n[SERVER] Processing...")

        if isinstance(data, bytes):
            print("[SERVER] Received encrypted data")
            return

        print(f"[SERVER] Amount: {data['amount']}")
        print(f"[SERVER] To: {data['to_account']}")
        print("[SERVER] Transaction completed")

# ---------------- MAIN ----------------
alice = Client()
eve = Attacker()
bank = Server()
defender = Defender()

print("="*50)
print("MITM SIMULATION (WITHOUT ENCRYPTION)")
print("="*50)

# Normal flow (attack happens)
msg = alice.send_message()
tampered = eve.intercept(msg)
bank.receive(tampered)

print("\n" + "="*50)
print("MITM SIMULATION (WITH ENCRYPTION)")
print("="*50)

# Secure flow
msg2 = alice.send_message()
encrypted_msg = defender.encrypt(msg2)
tampered2 = eve.intercept(encrypted_msg)
bank.receive(tampered2)