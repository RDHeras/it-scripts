import socket

# Target host (127.0.0.1 is localhost / your own computer for safe testing)
target_host = "127.0.0.1"

# Common network ports to scan (FTP, SSH, HTTP, HTTPS, Web Proxy)
ports_to_scan = [21, 22, 80, 443, 8080]

print(f"--- Starting Port Scan on {target_host} ---\n")

# Loop through each port in our list
for port in ports_to_scan:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a 1-second timeout
    s.settimeout(1.0)
  
    # Attempt to connect to the target port
    result = s.connect_ex((target_host, port))

    # If connection succeeds, the port is open
    if result == 0:
       print(f"[+] Port {port}: OPEN")
    else:
       print(f"[-] Port {port}: Closed")

    # Close the socket
    s.close()

print("\n--- Scan Complete ---")
