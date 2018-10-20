import sys
import socket

def whois():
    host = raw_input("host<( ")
    try:
        ip = socket.gethostbyname(host)
        sockt = socket.socket()
        sockt.connect(("whois.arin.net", 43))
        sockt.send(ip + "\r\n")

        response = ""
        while True:
            data = sockt.recv(4096)
            response += data
            if not data:
                break
        sockt.close()

        print '\t   +------------Details---------------+'
        print response
    except:
        print 'Error ocurred'

