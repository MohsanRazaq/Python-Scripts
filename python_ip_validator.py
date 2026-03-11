'''
The Challenge:
using only basics functionality of python
Take an IP string like "192.168.1.50".

Use .split('.') to get the four numbers.

Use a loop to check if each number is between 0 and 255.

Now we will do manuall checking but in future we will do automation
------------------------------------------------------------------------------------
| Input,            Expected Result        Logic Tested                             |
| 8.8.8.8,          Valid                 Standard IPv4 format                      |
| 10.0.0.256        Invalid               Out of range (>255)                       |
| 172.16.0,n        Invalid               Incorrect octet count (3 instead of 4)    |
| 192.168.1.one     Invalid              Non-digit characters (ValueError check)    |
| ...               Invalid              Empty octets                               |
|                                                                                   |
------------------------------------------------------------------------------------
'''
user_ip=input('Enter ip You want to Validate: ')
is_valid=True
ip=user_ip.split(".")
# we  split ip address by , and save  remaining as sring list.
if len(ip)!=4: #  as we know there must be 4 octets, so we check here
    is_valid=False
else:
    for i in ip:
        try:
            value=int(i) # we cant compare string with integer so we  typecast string  into integer

            if value<0 or value>255:
                    is_valid=False
                        
        except ValueError:
            print('Ip must be Digits')
            is_valid=False
            
                 
if is_valid:
    print(f'The {user_ip} is Valid..')
else:
    print(f'The {user_ip} is  Not Valid..')
