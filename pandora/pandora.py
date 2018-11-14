#!/usr/bin/env python
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
from tools.file_reader import *
from tools.tools_help import *

main_banner()
while True:
    try:
        pan = input('pan<( ')
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

            elif pan[1] == 'file_reader':
                f_reader()
            
            else:
                print('\33[91m[-]invalid argument for command\33[00m(\33[92;1muse\33[00m)')


        elif 'exit' in pan:
            print('Exiting.... ')
            time.sleep(1.5)
            break

        elif pan[0] in ('restart', 'refresh'):
            print('Restarting terminal...')
            time.sleep(3)
            os.system('./Pandora')
            break
        
        elif 'banner' in pan:
            banner()

        elif 'clear' in pan:
            os.system('clear')

        elif 'help' in pan:
            if len(pan) == 1:
                help()
            elif len(pan) == 2:
                helper(pan[1])

        elif 'version' in pan:
            version()
        else:
            print('\33[91m[?]Unknown command\33[00m(\33[92;1m{}\33[00m)'.format(pan[0]))

    except:
        pass
