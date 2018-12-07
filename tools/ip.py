from tools.status import *
import socket
import requests

def ip(command):
    print_status("retrieving ip.....")
    if command == "myip":
        try:
            req = requests.get(r'http://jsonip.com')
            ip = req.json()['ip']
            print_msg("ip is {}".format(ip))
        except:
            print_error("could not retrieve ip")

    elif command == "":
        print_warning("please specify host")

    else:
        try:
            ip = socket.gethostbyname(command)
            print_msg("ip is {}".format(ip))
        except:
            print_error("could not retrieve ip")

