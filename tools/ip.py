from tools.status import *
import socket

def ip(host):
    print_status("checking host \33[94m{}\33[00m...".format(host))
    try:
        ip = socket.gethostbyname(host)
        print_success("ip for host is {}".format(ip))

    except:
        print_error("an error occured.Try again.")
        
        