#small script to get ip address of host

import socket

#function to check ip
def get_ip():
    host = raw_input("host<( ")
    #checking validity of host
    try:
        ip = socket.gethostbyname(host)
        print "Ip for (\33[94;1m{}\33[00m) is <(\33[92;1m{}\33[00m)> ".format(host, ip)
    except:
        print "\33[91;1m[!]Could not find host\33[00m (\33[94;1m{}\33[00m)".format(host)

