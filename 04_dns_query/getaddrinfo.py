import socket

def resolve_domain(domain_name):
    try:
        addresses = socket.getaddrinfo(domain_name, None)
        
        ip_addresses = set()
        for addr in addresses:
            ip_addresses.add(addr[4][0])
        
        print(f"IP address(es) for {domain_name}:")
        for ip in ip_addresses:
            print(ip)
    except socket.gaierror:
        print(f"Error: Unable to resolve domain name '{domain_name}'.")

def main():

    domain_name = input("Enter a domain name: ")
    resolve_domain(domain_name)

if __name__ == "__main__":
    main()

