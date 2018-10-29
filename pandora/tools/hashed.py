import md5
using = '\33[91;1musing\33[00m(\33[92;1mhash_cracker\33[00m) '

def decrypt():


    counter = 1

    hashtext = raw_input(using + '\33[94;1mdecrypt\33[00m ' + 'hashtext<( ')
    print '''Alternative wordlist files:
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
    '''
    filename = raw_input(using + '\33[94;1mdecrypt\33[00m ' + 'filename<( ')
    di = 'passfold/'

    try:
        contents = open(di + filename, 'r')
    except:
        print '\33[91;1m[-]file not found\33[00m'
        sys.exit()

    for password in contents :
        filemd5 = md5.new(password.strip()).hexdigest()
        print 'trying password (\33[92;1m{}\33[00m) from (\33[92;1m{}\33[00m)'.format(password.strip(), filename)
        counter += 1

        if hashtext == filemd5:
            print 'match found:\nPassword is <(\33[94;1m{}\33[00m'.format(password)
            break
    else:
        print '\33[91;1m[-]password not found\33[00m'


def encrypt():
    text = raw_input(using + '\33[94;1mencrypt\33[00m ' + 'text<( ')
    hashed = md5.new(text.encode('utf-8')).hexdigest()
    print hashed

def hasher():
    types = raw_input(using  + '(\33[94;1mencrypt\33[00m or \33[94;1mdecrypt\33[00m?)<( ')
    if types == 'decrypt' or types in ('d', 1):
        decrypt()

    elif types == 'encrypt' or types in ('e', 2):
        encrypt()

    else:
        print '\33[91;1m[-]Invalid choice\33[00m\nSelect either \33[94;1mencrypt\33[00m or \33[94;1mdecrypt\33[00m'




