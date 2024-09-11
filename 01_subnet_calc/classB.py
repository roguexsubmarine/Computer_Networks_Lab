def ip_to_binary(ip):
    binary_ip = ""
    octets = ip.split('.')
  #  print("ip in list : ", octets)

    for octet in octets:
        binary_octet = bin(int(octet))[2:].zfill(8)
        binary_ip += binary_octet
    #print("binary_ip : ", binary_ip)
    return binary_ip



def binary_to_ip(binary):
    ip = []
    
    for i in range(0, 32, 8):
        binary_octet = binary[i:i+8]
        ip.append(str(int(binary_octet, 2)))
    
    return '.'.join(ip)


def calculate_network_broadcast(ip, subnet_mask):
    
    ip_bin = ip_to_binary(ip)
    subnet_bin = ["0"] * 32  # Initialize a list of 32 '0's
    for i in range(int(subnet_mask)):
        subnet_bin[i] = '1'
    subnet_bin = "".join(subnet_bin)  # Convert the list back to a string

    #print("subnet_mask : ", subnet_bin)

    subnet_id = binary_to_ip(subnet_bin)
    print("subnet_mask : ", subnet_id)

    number_of_networks = 2**(int(subnet_mask) - 16)
    print("number of subnets : ", number_of_networks)

    number_of_hosts = 2**(32 - int(subnet_mask))
    print("Number of Hosts : ", number_of_hosts - 2)

    network_id_bin = ""
    for i in range(32):
        network_id_bin += '1' if ip_bin[i] == '1' and subnet_bin[i] == '1' else '0'
    
    #print("network_id : ", network_id_bin)


    broadcast_bin = ""
    for i in range(32):
        broadcast_bin += '1' if ip_bin[i] == '1' or subnet_bin[i] == '0' else '0'
    
    #print("broadcast_id : ", broadcast_bin)

    network_id = binary_to_ip(network_id_bin)
    broadcast_address = binary_to_ip(broadcast_bin)
    
    return network_id, broadcast_address



def ip_to_int(ip):
    octets = ip.split('.')
    ip_int = 0
    for i in range(4):
        ip_int = ip_int * 256 + int(octets[i])
    
    return ip_int

def int_to_ip(ip_int):
    octets = []
    for _ in range(4):
        octets.append(str(ip_int % 256))
        ip_int //= 256

    return '.'.join(reversed(octets))



def main():
   
    subnet_mask = int(input("Enter the subnet mask (16 - 30): /"))
    while subnet_mask < 16 or subnet_mask > 30:
        print("Enter valid subnet mask !")
        subnet_mask = int(input("Enter the subnet mask (16 to 30): /"))

    ip_temp = ['0','0','0','0']
    while(int(ip_temp[0]) < 128 or int(ip_temp[0]) > 191):
        ip_address = input("Enter the IP address : ")
        ip_temp = ip_address.split('.')
    
    print("")
    
    

    network_id, broadcast_address = calculate_network_broadcast(ip_address, subnet_mask)
    
    network_id_int = ip_to_int(network_id)
    broadcast_address_int = ip_to_int(broadcast_address)
    
    first_usable_ip_int = network_id_int + 1
    last_usable_ip_int = broadcast_address_int - 1

    
    first_usable_ip = int_to_ip(first_usable_ip_int)
    last_usable_ip = int_to_ip(last_usable_ip_int)
    
    # print(f"IP Address: {ip_address}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Network ID: {network_id}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"\nChannel range from {first_usable_ip} to {last_usable_ip}")

if __name__ == "__main__":
    main()

