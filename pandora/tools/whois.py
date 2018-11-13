import sys
import socket

def whois():
    using = "\33[91;1musing\33[00m(\33[92;1mwhois\33[00m) "
    host = input(using + "host<( ")
    ip = socket.gethostbyname(host)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.arin.net", 43))
    
    s.send((ip + "\r\n").encode())
    
    response = b""
    while True:
        data = s.recv(4096)
        response += data
        if not data:
            break
    s.close()

    print("\t+---------------Details---------------+")
    print(response.decode())