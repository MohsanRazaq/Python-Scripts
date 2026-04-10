# 🔐 MITM Attack Simulation (Python)

## 📌 Project Overview

This project demonstrates a **Man-in-the-Middle (MITM) attack simulation** in Python, showing both:

* 🔴 **Insecure communication (no encryption)**
* 🟢 **Secure communication (with encryption)**

It is designed to help students understand how attackers intercept data and how encryption prevents such attacks.

---

## ⚠️ Ethical Disclaimer

This project is strictly for **educational and lab use only**.

* ✅ Use in **controlled environments only**
* ✅ For cybersecurity learning & research
* ❌ Do NOT use on real systems/networks without permission
* ❌ Unauthorized use may be illegal

---

## 🧠 Concept Diagram

### 🔴 Without Encryption (Vulnerable)

```
Client  ───────►  Attacker (EVE)  ───────►  Server
           (Intercept + Read + Modify)
```

👉 Attacker can:

* Read sensitive data (passwords, transactions)
* Modify transaction details

---

### 🟢 With Encryption (Secure)

```
Client  ───────►  Attacker (EVE)  ───────►  Server
        (Encrypted Data – Cannot Read)
```

👉 Attacker:

* Cannot understand encrypted data
* Cannot modify meaningful content

---

## ⚙️ Features

* 🔐 Encryption using `Fernet` (symmetric encryption)
* 🕵️ MITM interception simulation
* 📊 Logging of intercepted data
* 🔁 Comparison between secure & insecure communication

---

## 🧪 Sample Output

### 🔴 Attack Successful (No Encryption)

```
[EVE] username: noni_pk
[EVE] password: SecureP@ss123
[EVE] amount: 5000

[EVE] Tampering data...

[SERVER] Amount: 99999
[SERVER] To: EVE-4567
```

---

### 🟢 Attack Prevented (With Encryption)

```
[EVE] Encrypted data captured (cannot read)

[SERVER] Received encrypted data
```

---

## 🧩 Code Structure

| Component  | Role                       |
| ---------- | -------------------------- |
| `Client`   | Sends transaction data     |
| `Attacker` | Intercepts & modifies data |
| `Defender` | Encrypts/Decrypts messages |
| `Server`   | Processes transactions     |

---

## 🚀 Installation & Usage

### 1️⃣ Install Dependencies

```bash
pip install cryptography
```

### 2️⃣ Run Script

```bash
python mitm_simulation.py
```

---

## 📊 What You Will Learn

* MITM attack workflow
* Risks of plaintext communication
* Importance of encryption
* Basic secure communication design

---

## 🔐 Security Takeaways

* Never send sensitive data without encryption
* Use secure protocols (HTTPS, TLS)
* Always validate and protect communication channels

---

## 🔒 Safe Usage Guidelines

* Run only in:

  * Virtual machines
  * Isolated lab environments

* Do NOT:

  * Use on real banking systems
  * Test on public networks

---

## 📚 Academic Use

Ideal for:

* Cybersecurity students
* Network security labs
* Ethical hacking practice

---

## 👨‍💻 Author

**Mohsan Razaq**

---

## 📎 License

This project is licensed for **educational use only**.
