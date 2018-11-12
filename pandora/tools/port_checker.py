#imports
import socket
import time

#main port checking function
def port_checker():
    using = "\33[91;1musing\33[00m(\33[92;1mport_checker\33[00m) "
    count = 5
    ip = ''
    #getting host as input
    host = input(using + "host<( ")
    try:
        #getting ip of host
        ip = socket.gethostbyname(host)
        while True:
            sockt = socket.socket()
            #getting port as input
            port = int(input(using + "port<( "))
            if port in ('quit', 'exit'):
                print('exiting... ')
                time.sleep(1)
                break
            results = sockt.connect_ex((ip, int(port)))
            time.sleep(1)
            if results == 0:
                print("[+]port {} for <(\33[94;1m{}\33[00m)> is \33[92;1mopen\33[00m".format(port, host))
                count -= 1
            else:
                print("[-]port {} for <(\33[94;1m{}\33[00m)> is \33[91;1mclosed\33[00m".format(port, host))
                count -= 1
            if count == 0:
                print('Exiting ...')
                time.sleep(1)
                break

    except:
        print("\33[93;1m[?]Check input\33[00m")
