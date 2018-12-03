def print_status(msg):
    print("\33[94m[*]\33[00m" + msg)

def print_error(msg):
    print("\33[91m[-]\33[00m" + msg)

def print_warning(msg):
    print("\33[91m[!]\33[00m" + msg)

def print_success(msg):
    print("\33[92m[+]\33[00m" + msg)

def print_inloop(msg):
    print("\33[94m[~]\33[00m" + msg)

def print_msg(msg):
    print("\33[92m[>]\33[00m" + msg)