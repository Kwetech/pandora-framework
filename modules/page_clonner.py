#necessary imports
from tools.status import *
import requests
import time
import os

#function to clone webpage
check = False
def clone_page(url):
    global check
    #checking if url is valid
    if(url.startswith('http://')):
        urli = url
    else:

        urli = 'http://' + url
    try:
        #try to read url or page
        print_status('clonning \33[94m{}\33[00m'.format(urli))
        cont = requests.get(urli)
        check = True
        print_success('page successfully cloned')
        return cont.text
    except:
        print_error('Could not find page')
        check = False
        return 0


#function to save file to directory
def save_file(contents, file_name):

    #turning it into html file
    if(file_name.endswith('.html')):
        pass
    else:
        file_name += '.html'

    if contents != 0:
        #saving to dorectory
        di = os.getcwd()
        f = open(di+'/saves/'+file_name,'w+')
    
        f.write(contents)
        print_success('Page successfully saved')
        print_msg("file saved to '{}'".format('~/pandora-framework/saves/' + file_name))
    else:
        pass

#method to start clonning
def start_clonner():
    using = "\33[91musing\33[00m(\33[92;1mpage_clonner\33[00m) "
    url = input(using + "url<( ")
    contents = clone_page(url)
    if check == True:
        file_name = input(using + "file_name<( ")
        save_file(contents, file_name)
    else:
        pass
