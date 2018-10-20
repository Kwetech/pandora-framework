#!/usr/bin/env python
from tools.banner import *
from tools.ddos import *
from tools.get_ip import *
from tools.help import *
from tools.listener import *
from tools.page_clonner import *
from tools.port_checker import *
from tools.port_scanner import *
from tools.version import *
from tools.whois import *

main_banner()
while True:
    try:
        pan = raw_input('\33[1mpan<( ')
        
        if pan == 'banner':
            banner()

        elif pan == 'exit':
            print 'Exiting.... '
            time.sleep(1.5)
            break

        elif pan == 'clear':
            os.system('clear')

        elif pan == 'ddos':
            ddos()

        elif pan == 'ip':
            get_ip()

        elif pan == 'help':
            help()

        elif pan == 'listener':
            listener()

        elif pan == 'clone':
            start_clonner()

        elif pan == 'portcheck':
            port_checker()

        elif pan == 'portscan':
            port_scanner()

        elif pan == 'version':
            version()

        elif pan == 'whois':
            whois()
            
        else:
            '\33[91;1m[?]Unknown command\33[00m'

    except:
        pass
