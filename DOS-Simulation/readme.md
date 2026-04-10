# DoS Simulation Project (Controlled Lab – Educational Use Only)

## 📌 Overview

This project demonstrates a **Denial-of-Service (DoS) simulation** in a **controlled lab environment**. It is designed to help students understand how high volumes of requests impact system performance, availability, and response behavior.

---

## ⚠️ Ethical Use Disclaimer

This project is intended **strictly for educational and research purposes**.

* ✅ Use only in a **controlled lab environment**
* ✅ Test only on systems you **own or have explicit permission to use**
* ❌ Do NOT use against public servers, networks, or unauthorized systems
* ❌ Any misuse may be illegal and unethical

---

## 🎯 Learning Objectives

This simulation helps you understand:

* Behavior of systems under heavy load
* Impact of concurrent requests (threads)
* Basics of DoS attack patterns (conceptual level)
* Performance monitoring and analysis

---

## 🧪 Sample Output

```
==============================
SIMULATION SUMMARY
==============================
Total Threads       : 50
Successful Requests : 38
Failed Requests     : 12
Time Elapsed (s)    : 7.13
Avg Req/sec         : 7.02
Min Response Time   : 2.1583 s
Max Response Time   : 5.1732 s
Avg Response Time   : 3.0875 s
==============================
```

---

## 📊 Output Explanation

* **Total Threads** → Number of concurrent simulated requests
* **Successful Requests** → Requests completed without failure
* **Failed Requests** → Requests dropped or failed due to load
* **Time Elapsed** → Total duration of the simulation
* **Avg Req/sec** → Throughput of the system under load
* **Min Response Time** → Fastest response observed
* **Max Response Time** → Slowest response observed
* **Avg Response Time** → Average response delay

---

## 🧠 Key Observations

* As thread count increases, **system load increases**
* Higher load may cause **request failures and latency spikes**
* Response time variation shows **system stability under stress**

---

## 🛠️ Usage

1. Run the simulation script in your lab environment

2. Monitor output in terminal

3. Adjust parameters like:

   * Thread count
   * Request rate
   * Delay intervals

4. Analyze how system performance changes

---

## 🔐 Safety Guidelines

* Always run inside:

  * Virtual machine
  * Isolated lab network
* Avoid using real production systems
* Monitor resource usage (CPU, RAM, Network)

---

## 📚 Academic Note

This project is part of **cybersecurity learning**, focusing on understanding attack behavior to improve **defensive strategies**.

---

## 📎 License

This project is provided for **educational and research purposes only**.
