import socket

dns_table = {
    'example.com': '93.184.216.34',  # Example domain and IP
    'google.com': '8.8.8.8',         # Google Public DNS IP
    'openai.com': '104.18.6.34',     # OpenAI domain and IP
    'github.com': '140.82.121.4',    # GitHub domain and IP
    'yahoo.com': '98.137.11.163',    # Yahoo domain and IP
    'bing.com': '204.79.197.200',    # Bing domain and IP
    'facebook.com': '157.240.22.35', # Facebook domain and IP
    'amazon.com': '205.251.242.103', # Amazon domain and IP
}   
    
def dns_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Starting server...")
    s.bind(("127.0.0.1", 1234))

    while True:
        data, addr = s.recvfrom(1024)
        domain_name = data.decode().strip()
        
        if domain_name == "EXIT":
            print("Shutting down server...")
            break
        
        print(f"{addr} requesting {domain_name}!")
        ip = dns_table.get(domain_name, "NOT FOUND!!")

        s.sendto(ip.encode(), addr)
    s.close()

if __name__ == "__main__":
    dns_server()