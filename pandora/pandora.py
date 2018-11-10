#!/usr/bin/env python2
from tools.banner import *
from tools.get_ip import *
from tools.help import *
from tools.listener import *
from tools.page_clonner import *
from tools.port_checker import *
from tools.port_scanner import *
from tools.version import *
from tools.whois import *
from tools.subdomain_finder import *
from tools.ddos import *
from tools.hashed import *

main_banner()
while True:
    try:
        pan = raw_input('\33[1mpan<( ')
        pan = pan.split()
        
        if pan[0] == 'use':

            if pan[1] == 'ip':
                get_ip()

            elif pan[1] == 'listener':
                listener()

            elif pan[1] == 'page_clonner':
                start_clonner()

            elif pan[1] == 'port_checker':
                port_checker()

            elif pan[1] == 'port_scanner':
                port_scanner()

            elif pan[1] == 'whois':
                whois()

            elif pan[1] == 'subdomain_finder':
                subdomains()

            elif pan[1] == 'ddos':
                ddos()

            elif pan[1] == 'hasher':
                hasher()
            
            else:
                print '\33[91;1m[-]invalid argument for command\33[00m(\33[92;1muse\33[00m).'


        elif 'exit' in pan:
            print 'Exiting.... '
            time.sleep(1.5)
            break
        
        elif 'banner' in pan:
            banner()

        elif 'clear' in pan:
            os.system('clear')

        elif 'help' in pan:
            help()

        elif 'version' in pan:
            version()
        else:
            '\33[91;1m[?]Unknown command\33[00m'

    except:
        pass
