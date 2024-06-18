import socket
from IPy import IP

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress,port))
        print('[+] port'+str(port)+'is Open')
    except:
        print('[-] port' + str(port)+'is Closed')

ipaddress = input('[+] Enter target to scan:')
for port in range(70,90):
  scan_port(ipaddress,port)