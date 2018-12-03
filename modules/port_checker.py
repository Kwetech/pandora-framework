#imports
import socket
import time
from tools.status import *

#main port checking function
def port_checker():
    using = "\33[91musing\33[00m(\33[92;1mport_checker\33[00m) "
    count = 5
    #getting host as input
    host = input(using + "host<( ")
    try:
        #getting ip of host
        ip = socket.gethostbyname(host)
        while True:
            sockt = socket.socket()
            #getting port as input
            port = input(using + "port<( ")
            if port in ('quit', 'exit'):
                print_status('exiting... ')
                time.sleep(1)
                break
            results = sockt.connect_ex((ip, int(port)))
            time.sleep(1)
            if results == 0:
                print_success("port {} for \33[94m{}\33[00m is \33[92mopen\33[00m".format(port, host))
                count -= 1
            else:
                print_error("port {} for \33[94m{}\33[00m is \33[91mclosed\33[00m".format(port, host))
                count -= 1
            if count == 0:
                print_status('exiting ...')
                time.sleep(1)
                break

    except:
        print_warning("Check input")
