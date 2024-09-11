import socket

def client():

    hostname = socket.gethostname()
    ipaddr = "127.0.0.1"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (ipaddr, 1234)
    c = "y"

    while c.upper() == "Y":
        req_domain = input("Enter Domain name: ")

        send = s.sendto(req_domain.encode(), addr)
        data, address = s.recvfrom(1024)
        reply_ip = data.decode().strip()
        print(f"The IP of {req_domain} is {reply_ip}")

        req_domain = None

        c = input("Continue (y/n): ")

    s.sendto("EXIT".encode(), addr)

    s.close()

if __name__ == "__main__":
    client()
