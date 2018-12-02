def f_reader():
    using = '\33[91musing\33[00m(\33[92;1mfile_reader\33[00m) '
    filename = input(using + 'file_name<( ')
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except:
        print('[-]unable to locate file')
    