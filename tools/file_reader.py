from tools.status import *
import time
def f_reader(filename):
    print_status("reading from file \33[94m{}\33[00m\n".format(filename))
    time.sleep(3)
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except:
        print_error('unable to locate file')
    