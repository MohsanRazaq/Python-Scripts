# ============================================================
# DoS Attack Simulation (SAFE - For Learning Only)
# Target: httpbin.org (public testing site)
# ============================================================

import requests
import threading
import time

# ---------------- CONFIG ----------------
URL = 'https://httpbin.org/get'   # Safe public endpoint
NUM_THREADS = 100   # Change for i-,+ number of threads

# ---------------- GLOBAL COUNTERS ----------------
success_count = 0
fail_count = 0
lock = threading.Lock()

# ---------------- STORE RESPONSE TIMES ----------------
response_times = []

# ---------------- FUNCTION ----------------
def send_request(thread_id):
    global success_count, fail_count
    
    try:
        start = time.time()
        response = requests.get(URL, timeout=5)
        end = time.time()

        with lock:
            success_count += 1
            response_times.append(end - start)
            print(f"[Thread {thread_id:03d}] HTTP {response.status_code}")

    except requests.exceptions.Timeout:
        with lock:
            fail_count += 1
            print(f"[Thread {thread_id:03d}] TIMEOUT")

    except requests.exceptions.RequestException as e:
        with lock:
            fail_count += 1
            print(f"[Thread {thread_id:03d}] ERROR: {e}")

# ---------------- MAIN ----------------
print(f"\nStarting DoS Simulation with {NUM_THREADS} threads...\n")

start_time = time.time()

threads = []

for i in range(NUM_THREADS):
    t = threading.Thread(target=send_request, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

# ---------------- SUMMARY ----------------
elapsed = time.time() - start_time

print("\n" + "="*50)
print("SIMULATION SUMMARY")
print("="*50)
print(f"Total Threads       : {NUM_THREADS}")
print(f"Successful Requests : {success_count}")
print(f"Failed Requests     : {fail_count}")
print(f"Time Elapsed (s)    : {elapsed:.2f}")
print(f"Avg Req/sec         : {NUM_THREADS/elapsed:.2f}")

# Response time stats
if response_times:
    print(f"Min Response Time   : {min(response_times):.4f} s")
    print(f"Max Response Time   : {max(response_times):.4f} s")
    print(f"Avg Response Time   : {sum(response_times)/len(response_times):.4f} s")

print("="*50)