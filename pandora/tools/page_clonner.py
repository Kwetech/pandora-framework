#necessary imports
import urllib
import time
import os

#function to clone webpage
def clone_page(url):
    #checking if url is valid
    if(url.startswith('http://')):
        urli = url
    else:

        urli = 'http://' + url
    try:
        #try to read url or page
        print 'clonning into (\33[94;1m{}\33[00m)'.format(urli)
        cont = urllib.urlopen(urli).read()
        return cont
    except:
        print '\33[91;1m[-]Error could not find page\33[00m'
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
        print '\33[92;1m[+]page successfully saved\33[00m'
    else:
        pass

#method to start clonning
def start_clonner():
    using = "\33[91;1musing\33[00m(\33[92;1mpage_clonner\33[00m) "
    url = raw_input(using + "url<( ")
    contents = clone_page(url)
    file_name = raw_input(using + "file_name<( ")
    save_file(contents, file_name)
