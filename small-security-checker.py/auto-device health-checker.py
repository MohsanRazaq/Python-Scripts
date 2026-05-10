import os
import subprocess

def daily_security_check():
    print("--- Starting System Check ---")
    
    ip_info = subprocess.check_output(["hostname", "-I"]).decode()
    print(f"Your IP Address is: {ip_info}")
    disk = os.popen('df -h / | grep /').read()
    print(f"Disk Status: {disk}")

    with open("security_log.txt", "a") as f:
        f.write(f"Check performed. IP: {ip_info}")

daily_security_check()