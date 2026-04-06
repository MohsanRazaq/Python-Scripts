# Dictionary to store login attempts
attempts = {}

ip = "192.168.1.1"

# Simulate 5 login attempts
for i in range(5):
    
    # Increase attempt count
    attempts[ip] = attempts.get(ip, 0) + 1
     
    # Check if blocked
    if attempts[ip] > 3:
        print("IP blocked:", ip)  
        break
    else:
        print("Login failed attempt", attempts[ip])
