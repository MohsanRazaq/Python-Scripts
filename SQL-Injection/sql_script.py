# ============================================================
# SQL Injection Simulation
# ============================================================

import sqlite3

# Creating temporary database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Creating table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    role TEXT
)
''')

# Inserting your own style data (not default names)
cursor.execute("INSERT INTO users VALUES (1, 'mohsan', 'mohsan123', 'user')")
cursor.execute("INSERT INTO users VALUES (2, 'admin_mohsan', 'secure@123', 'admin')")
cursor.execute("INSERT INTO users VALUES (3, 'guest_mohsan', 'guest123', 'user')")
conn.commit()

# Login function
def login(username, password, safe_mode=False):
    print("\n------------------------------")
    print("Username:", username)
    print("Password:", password)

    if safe_mode:
        print("Mode: SAFE")
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
    else:
        print("Mode: VULNERABLE")
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        print("SQL:", query)
        cursor.execute(query)

    result = cursor.fetchall()

    if result:
        print("✔ LOGIN SUCCESS")
        for row in result:
            print("User:", row[1], "| Role:", row[3])
    else:
        print("✘ LOGIN FAILED")


# ---------------- TEST CASES ----------------

print("TEST 1: Valid Login")
login('mohsan', 'mohsan123')

print("\nTEST 2: Wrong Password")
login('mohsan', 'wrongpass')

print("\nTEST 3: SQL Injection (Bypass)")
login('admin_mohsan', "' OR '1'='1")

print("\nTEST 4: SQL Injection (Dump All)")
login("' OR 1=1 --", 'anything')

print("\nTEST 5: Safe Mode")
login("' OR 1=1 --", 'anything', safe_mode=True)