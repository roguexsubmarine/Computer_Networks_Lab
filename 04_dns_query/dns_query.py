import sys
import socket

def resolve_hostname(hostname):
    try:
        # Perform DNS query to get the IP address
        ip_address = socket.gethostbyname(hostname)
        print(f"IP address of {hostname}: {ip_address}")
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname '{hostname}'.")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <hostname>")
        return
    
    hostname = sys.argv[1]
    resolve_hostname(hostname)

if __name__ == "__main__":
    main()

