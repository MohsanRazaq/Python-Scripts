'''Task:
Dictionary: service_map = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL"}

List: found_ports = [22, 80, 9000, 443, 21]

Loop: Iterate through found_ports.

Logic: * If the port is a Key in your dictionary, print its Value.

If not, print "UNKNOWN".
'''
service_map = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL"}
found_ports = [22, 80, 9000, 443, 21]
''''
we will use here get() method  to get our value from dict..we can also do this by loop

'''
# by get () method
print('---By Get() method---')
for port in found_ports:
    print(f'The {service_map.get(port,"Unknown Services")} is running on port  {port}')
    
#---------------------------------------------------------------------------------------- 
print('---By Get() method---')  #by Loop 
for port in found_ports:
    if port in service_map:
        service=service_map[port]
        print(f'The Service {service} is running on port {port}')
    else:
        print(f'The UnKnown Service is running on port {port}')
        
