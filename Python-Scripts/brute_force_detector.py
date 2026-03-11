'''
Task:
Write a Python script that:
Opens the auth.log file in "read" mode.
Iterates through every line using a for loop.
Splits each line at the comma , to separate the IP from the Status.
Filters: Only look for lines where the status is "FAILED".
Logic: Count how many times each IP failed. If an IP fails more than 3 times,
print: [ALERT] Brute Force detected from IP: 10.0.0.5.
'''
''' 
if this path not working then try 
    import os 
    script_dir = os.path.dirname(__file__) 
    log_path = os.path.join(script_dir, "logs.txt")
    then  with open(log_path, 'r') as f:  remaining code
    '''
    
failed_attempts={}
try:
    with open("logs.txt", 'r') as f: 
        for line in f:
            data = line.strip().split(",")
            if len(data) == 2:
                    ip = data[0]   
                    status = data[1]
                    if status == "FAILED":
                        if  ip in failed_attempts:
                            failed_attempts[ip] += 1
                        else:
                            failed_attempts[ip] = 1
            else:
                print(f"Skipping invalid line: {line.strip()}")
                    
    for attacker_ip in failed_attempts:
        count = failed_attempts[attacker_ip]
        if count > 3:
            with open("threat_report.txt", "a") as report:
                report.write(f"ALERT--> Brute Force: {attacker_ip} | Failures: {count}\n")
            print(f'ALERT--> Brute Force detected from Ip : {attacker_ip}')

except FileNotFoundError:
    print("Error: log file not found in  running  script directory.")