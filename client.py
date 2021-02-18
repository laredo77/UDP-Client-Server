import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    val = bytes(input(""), 'utf-8')  # Enter address
    s.sendto(val, (sys.argv[1], int(sys.argv[2])))
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8').split(',')[1])
