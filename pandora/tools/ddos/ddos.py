import os

def ddos():
    using = '\33[91;1musing\33[00m(\33[92;1mddos\33[00m) '
    host = raw_input(using + 'host<( ')
    port = input(using + 'port<( ')
    num_request = input(using + 'requests<( ')
    os.system('python2 ~/Pandora-Framework/pandora/tools/ddos/main_ddos.py' + host + port + num_requests)
