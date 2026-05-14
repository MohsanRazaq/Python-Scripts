'''Task:
Dictionary: service_map = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL"}

List: found_ports = [22, 80, 9000, 443, 21]

Loop: Iterate through found_ports.

Logic: * If the port is a Key in your dictionary, print its Value.

If not, print "UNKNOWN".
'''
# ================================
# Simple Port-Service Identifier
# ================================

service_map = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

found_ports = [22, 80, 9000, 443, 21]


print("=" * 40)
print("      PORT SCAN RESULTS")
print("=" * 40)

for port in found_ports:

    service = service_map.get(port, "UNKNOWN")

    status = (
        f"[+] Port {port:<5} | Service : {service}"
        if service != "UNKNOWN"
        else f"[-] Port {port:<5} | Service : UNKNOWN"
    )

    print(status)

print("=" * 40)
