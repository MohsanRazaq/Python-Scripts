'''
The Setup:

🛠️ Project 1: The "Unique IP" Deduplicator
Create a file named raw_ips.txt.
Let's start your 5-project challenge. This is a common task when a security tool gives you 10,000 lines of data, but only 5 IPs are actually involved.
The Setup:
Create a file named raw_ips.txt.
#The Task:

Read the file line by line.

Use a List called unique_ips.

As you loop, check if the IP is NOT in unique_ips.

If it's new, append it.

At the end, print how many total IPs you started with vs. 
how many unique ones you found

if this path not working then try 
    import os 
    script_dir = os.path.dirname(__file__) 
    log_path = os.path.join(script_dir, "raw_ips.txt")
    then  with open(log_path, 'r') as f:  remaining code
'''
all_ips=[]
duplicate=0
unique_ips=[]
with open("raw_ips.txt",'r') as f:
    all_ips=f.readlines()
for ip in all_ips:
    c_ip=ip.strip()
    if c_ip not in unique_ips:
        unique_ips.append(c_ip)
    else:
        duplicate+=1
        

print(f"All Ip's : {len(all_ips)}\nUnique Ip's: {len(unique_ips)}\nDuplicates Found: {duplicate}")