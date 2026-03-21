'''

DEFINE base_network = "192.168.1."

CREATE empty list active_hosts

FOR i from 1 to 254:
    ip = base_network + i

    SEND 1 ping request to ip with short timeout

    IF response received:
        ADD ip to active_hosts
        PRINT ip is active

RETURN active_hosts

'''
import  os
def live_host(url):
    active_host=[]
    for i in range(1,10):
        ip=url+str(i)
        response=os.system(f"ping -c 1  -W 1 {ip}")
        #response = os.system(f"ping -c 1 -W 1 {ip} > dev/null 2>&1")
        if response == 0:
            print(f"[+] Active: {ip}")
            active_host.append(ip)
    print(f"Following host are Active: /n{active_host}")
    
import socket

def find_ports(ip):
    open_ports = []
    
    for port in [22, 80, 443]:
        s = socket.socket()
        s.settimeout(0.5)
        
        try:
            s.connect((ip, port))
            open_ports.append(port)
        except:
            pass
        
        s.close()
    
    return open_ports
url="192.168.100.6"
print(find_ports(url))