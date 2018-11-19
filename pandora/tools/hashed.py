import hashlib, os,sys
using = '\33[91musing\33[00m(\33[92;1mhash_cracker\33[00m) '
def decrypt():
    hashtext = input(using + '\33[94mdecrypt\33[00m ' + 'hashtext<( ')
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
    filename = input(using + '\33[94mdecrypt\33[00m ' + 'filename<( ')
    di = 'passfold/'
    try:
        contents = open(di + filename, 'r')
    except:
        print('\33[91m[-]file not found\33[00m')
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
            print('[~]trying password (\33[92m{}\33[00m) from (\33[92m{}\33[00m)'.format(password, filename))
            if hashtext == filem:
                print('match found:\nPassword is <(\33[94m{}\33[00m)>'.format(password.strip()))
                break
        else:
            print('[-]Hash type not supported')
            break
    else:
        print('\33[91;1m[-]password not found\33[00m')
def encrypt():
    text = input(using + '\33[94mencrypt\33[00m ' + 'text<( ')
    hashed = hashlib.md5(text.encode('utf-8')).hexdigest()
    print(hashed)
def hasher():
    types = input(using  + '(\33[94mencrypt\33[00m or \33[94mdecrypt\33[00m?)<( ')
    if types == 'decrypt' or types in ('d', 1):
        decrypt()
    elif types == 'encrypt' or types in ('e', 2):
        encrypt()
    else:
        print('\33[91m[-]Invalid choice\33[00m\nSelect either \33[94;1mencrypt\33[00m or \33[94;1mdecrypt\33[00m')
