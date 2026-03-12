''''
Requirements:
File Reading: Open network_logs.txt and read it line-by-line.

Lists: Create a list called blocked_ips to store every IP that has a "BLOCK" status.

Dictionaries: Create a dictionary called incident_count.

Logic: Loop through your blocked_ips list and count how many times each IP appears (e.g., {"10.0.0.5": 3}).

Nested Logic: * If an IP has been blocked more than 2 times, print a "CRITICAL" alert.

If it's blocked 1-2 times, print a "WARNING".

Final Output: Print the total number of unique attackers found.
'''
all_blocked=[]
incident_report={}
with open("network_logs.txt",'r') as f:
    data= f.readlines()
for i in data:
    parts=i.strip().split(",")
    ip=parts[0]
    status=parts[1]
    if status=="BLOCK":
        all_blocked.append(ip)
for ip in all_blocked:
    if ip in incident_report:
        incident_report[ip]+=1
    else:
        incident_report[ip]=1
for ip in incident_report:
    count=incident_report[ip]
    if count> 2:
        print(f"  CRITICAL  {ip} blocked {count} times  \n")
    else:
        print(f"  WARNING  {ip} blocked {count} times \n")
      
unique_attackers = len(incident_report)
print(f" Total unique attackers are : {unique_attackers}")
        
        
   