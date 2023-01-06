import socket
domain_name = input("Enter Your Target:")

ip = socket.gethostbyname(domain_name)
print(ip)
