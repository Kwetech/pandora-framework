from tools.status import *
import hashlib, os,sys
using = '\33[91musing\33[00m(\33[94mhash_cracker\33[00m) '
def decrypt():
    hashtext = input(using + 'hashtext<( ')
    print('''Alternative wordlist files:
    password1.txt
    password2.txt
    password3.txt
    password4.txt
    password5.txt (Recommended)
    password6.txt
    allnames.txt
    keypass.txt
    mnames.txt
    fnames.txt
    ''')
    filename = input(using + 'filename<( ')
    di = 'passfold/'
    try:
        contents = open(di + filename, 'r')
    except:
        print_error('unable to find file')
        sys.exit()
    for password in contents:
        password = password.strip()
        if len(hashtext) == 32:
            filem = hashlib.md5(password.encode('utf-8')).hexdigest()
            
        elif len(hashtext) == 40:
            filem = hashlib.sha1(password.encode('utf-8')).hexdigest()

        elif len(hashtext) == 56:
            filem = hashlib.sha224(password.encode('utf-8')).hexdigest()

        elif len(hashtext) == 64:
            filem = hashlib.sha256(password.encode('utf-8')).hexdigest()

        elif len(hashtext) == 96:
            filem = hashlib.sha384(password.encode('utf-8')).hexdigest()

        elif len(hashtext) == 128:
            filem = hashlib.sha512(password.encode('utf-8')).hexdigest()

        else:
            filem = None


        if filem is not None:
            print_inloop('trying password (\33[92m{}\33[00m) from (\33[92m{}\33[00m)'.format(password, filename))
            if hashtext == filem:
                print_success('match found:\nPassword is <(\33[94m{}\33[00m)>'.format(password.strip()))
                break
        else:
            print_warning('Hash type not supported')
            break
    else:
        print_error('password not found')