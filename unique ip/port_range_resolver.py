'''
🛠️ Task: The "Nmap-Style" Port Range Resolver
📋 Scenario
In network security, tools like Nmap allow users to scan a range of ports using a dash (e.g., 21-25). 
However, computers don't understand the dash; they need a list of individual numbers to check.
Your mission:
Write a Python script that takes a string input, validates it for security and logic
and then "expands" that range into a list of usable integers.

'''
user_input=input("Enter Range of Ip: Ig..20-25 ")
if user_input.startswith("-"):
    print("Security Error: Ports cannot be negative numbers.")
else:
    
    user=user_input.split("-")
    if len(user)==2:
        try: 
            start=int(user[0])
            end=int(user[1])
            if (start <0 or start> 65535)  or   (end <0 or end > 65535):
                    print('Invalid Range.Must be between 0 65535')
            else:    
                if start<=end:
                    for i in range(start,end+1):
                        print(f'Range= {user_input}= range: {i}')
                else:
                    print('Start Must be less than end point')           
        except:
            print("Invalid Range Provided")
    else:
        print("invalid")
