from tools.status import *
import socket
import sys
import os
from datetime import datetime
import time


def port_scanner():
    using = "\33[91musing\33[00m(\33[94mport_scanner\33[00m) "
    try:
        host = input(using + 'host<( ')

        tm1 = datetime.now()
        s_port = input(using + 'start_port<( ')
        e_port = input(using + 'end_port<( ')

        ip = socket.gethostbyname(host)
        
        for port in range(int(s_port) ,int(e_port)+1):  
            sockt = socket.socket()
            results = sockt.connect_ex((ip, port))
            if results == 0:
                 print("Port {}    =>    \33[92mOpen\33[00m".format(port))
                 sockt.close()
        tm2 = datetime.now()
        tmcmp = tm2 - tm1
        print_msg("Scanning completed in:" + str(tmcmp))
    except:
        print_error('Error occured')
        print_status('exiting.... ')
        time.sleep(3)