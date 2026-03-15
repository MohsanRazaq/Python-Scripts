'''
Task:
You need to analyze access_logs.txt and identify "Power Users" (VIPs).

# 1. Open 'access_logs.txt' in read mode
# 2. Use the 'Name' as a key in 'access_counts' to count SUCCESS logins.
# 3. After the loop, check: If a name has > 2 logins, add them to 'vip_list'.
# Print the 'access_counts' dictionary and the 'vip_list'. 
'''
access_counts={}
vip_list=[]

with open("access.txt",'r') as f:
    data=f.readlines()  #---> List 
for name in data:
    f_name=name.strip().split(",")
    name=f_name[0]
    status=f_name[1]
    if status=="SUCCESS":
        if name in access_counts:
            access_counts[name]+=1
        else:
                access_counts[name]=1
                
for name in access_counts:
    if access_counts[name]>2:
        vip_list.append(name)
        
print('----------- SECURITY REPORT -----------')
print(f'           VIP Users : {", ".join(vip_list)}')
print('---------------------------------------')
print("Detailed Access Log:")
for user, count in access_counts.items():
    print(f"User: {user:11} | Logins: {count}")    
            