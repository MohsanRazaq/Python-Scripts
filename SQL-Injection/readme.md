#  SQL Injection Simulation (Python)

---

##  Project Overview

This project demonstrates a **SQL Injection (SQLi) attack simulation** using Python and SQLite. It clearly shows the difference between:

* **Vulnerable login system (unsafe queries)**
*  **Secure login system (parameterized queries)**

The simulation helps in understanding how attackers can exploit poorly written SQL queries and how to defend against such attacks.

---

##  Ethical Disclaimer

This project is developed strictly for **educational purposes**.

* ✅ Use only in **local or lab environments**
* ✅ For cybersecurity learning and practice
* ❌ Do NOT use on real applications or databases
* ❌ Unauthorized testing is illegal

---

##  Concept Overview

###  Vulnerable System

* Uses string-based SQL queries
* User input is directly injected into query
* Allows attackers to manipulate SQL logic

###  Secure System

* Uses parameterized queries (`?`)
* Input treated as data, not executable SQL
* Prevents SQL injection

---

##  Simulation Output

Below is a real execution example from the script:

```id="out1"
Username: mohsan
Password: wrongpass
Mode: VULNERABLE
SQL: SELECT * FROM users WHERE username='mohsan' AND password='wrongpass'
✘ LOGIN FAILED
```

---

###  SQL Injection (Bypass Authentication)

```id="out2"
Username: admin_mohsan
Password: ' OR '1'='1
Mode: VULNERABLE
SQL: SELECT * FROM users WHERE username='admin_mohsan' AND password='' OR '1'='1'
✔ LOGIN SUCCESS

User: mohsan | Role: user
User: admin_mohsan | Role: admin
User: guest_mohsan | Role: user
```

 **Attack Result:** Authentication bypassed, all users exposed

---

###  SQL Injection (Dump All Data)

```id="out3"
Username: ' OR 1=1 --
Password: anything
Mode: VULNERABLE
SQL: SELECT * FROM users WHERE username='' OR 1=1 -- ' AND password='anything'
✔ LOGIN SUCCESS

User: mohsan | Role: user
User: admin_mohsan | Role: admin
User: guest_mohsan | Role: user
```

 **Attack Result:** Entire database dumped

---

### 🛡️Safe Mode (Prevention)

```id="out4"
Username: ' OR 1=1 --
Password: anything
Mode: SAFE
✘ LOGIN FAILED
```

 **Defense Result:** Injection blocked successfully

---

## 📊Key Learnings

* SQL Injection occurs when:

  * User input is directly inserted into queries

* Attackers can:

  * Bypass login
  * Access sensitive data
  * Extract entire database

* Prevention:

  * Use **parameterized queries**
  * Never trust user input

---

##  Features

* 🧪 In-memory SQLite database
* 🔓 Vulnerable authentication system
* 🔐 Secure authentication (safe mode)
* 🧠 Multiple real-world attack scenarios
* 📊 Clear console output for learning

---

##  How to Run

```bash id="run1"
python sql_script.py
```

---

##  Security Best Practices

* Always use parameterized queries
* Avoid dynamic SQL construction
* Validate and sanitize inputs
* Use ORM frameworks where possible

---

##  Safe Usage Guidelines

* Run only in:

  * Local machine
  * Virtual lab

* Never:

  * Test on live websites
  * Use real credentials

---

##  Academic Use

Perfect for:

* Cybersecurity students
* Ethical hacking labs
* Database security learning

---

## 📎 License

This project is available for **educational and personal use only**.
