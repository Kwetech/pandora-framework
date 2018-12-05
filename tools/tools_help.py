from tools.status import *
def whois_help():
    print("""
    Tool Name: Whois Lookup

    ---+Description
    Used to perforn a whois lookup on a target
    website, it gathers basic information about
    your target website.

    ---+Usage
    type: \33[92;3muse whois \33[00min the Pandora prompt \33[1mpan<( \33[00m

    you should see a prompt looking same like this
    one \33[93;3musing(whois) url<( \33[00m

    type the name of the ip of the website or just
    type the name of the website and WHOIS will
    turn it into an IPv4 address,then press to
    see the whois lookup of your target website.

    example: \33[92;3mwww.examplesite.com\33[00m
        
  """)

def ddos_help():
    print("""
    Tool Name: Ddos

    ---+Description
    Used to perform a ddos attack on a website,
    it sends lot of packets to target website to
    slow it down or maybe crash weak websites.

    ---+Usage

    type: \33[92;3muse ddos\33[00m in the Pandora prompt \33[1mpan<(\33[00m
    type:
    1->the address of target webiste(e.g ip)
    2->the port to connect to (Rec. 80)
    3->the number of rewuests(Rec 100000+)
     
    Hit enter then wait for pandora to do the
     rest
   """)

def hash_cracker_help():
    print("""
    Tool Name: Hasher Cracker

    ---+Description
    It is used to decrypt or crack hashhed to 
    plain text.
    Supported hashes

    -md5 algorithm
    -sha1 algorithm
    -sha224 algorithm
    -sha256 algorithm
    -sha384 algorithm
    -sha512 algorithm


    ---+Usage.
    
    \33[94;4mDecrypt\33[00m
    To decrypt follow the steps:
    1->paste the hashed text onto the prompt
    2->choose 1 file from the altanatives filenames
    given type it and hit enter.
    Pandora will automatically detect hash type
    wait for Pandora to search the file for a word
    that matches the hashed text.
    if it outputs password not found repeat the 
    process and choose another file.
   """)



def listener_help():
    print("""
    Tool Name: Listener

    ---+Description
    It is used to listen to incoming connection from
    clients.

    ---+Usage
    type: \33[92;3muse listener\33[00m in the Pandora prompt \33[1mpan<( \33[00m
    1->type the ip address
    2->type the port you want to listen to
    Remember port number should be the same as
    the one in payload
    press enter then wait for connrctions from
    clients.After this you can execute shell
    commands to client.

    examlple:
    \33[93;3m<( 127.0.0.1
    <( 4444\33[00m
        
   """)



def page_clonner_help():
    print("""
    Tool Name: Page Clonner

    ---+Description
    It is used to clone wepgages or get the source
    HTML of a webpage.



    ---+Usage
    type:\33[92;3muse page_clonner\33[00m in the Pandora prompt \33[1mpan<( \33[00m
    1->type the url of the page you want to clone
    2->wait for Pandora to clone it then type the
    filename with the extension .html.
    Hit enter then go to saves or use the file_reader
    to read the contents.

    example:
    \33[93;3m<( http://www.example.com
    <( filename.html\33[00m
   """)



def port_scanner_help():
    print("""
    Tool Name: Port Scanner

    ---+Description
    It is used to scan open ports in range.


    ---+Usage
    type:\33[92;3muse port_scanner\33[00m in the Pandora prompt \33[1mpan<( \33[00m
    1->type the ip or address of target
    2->type the port you want to scan from
    3->type the port you want to scan to
    Hit enter then wait for Pandora to start 
    scanning.
    example:
    \33[93;3m<( example.com
    <( 1
    <( 150 \33[00m
     """)



def port_checker_help():
    print("""
    Tool Name: Port Checker

    ---+Description
    It used to check open ports in singles.
    Rather than wasting time scanning in range
    you can check it in singles

    ---+Usage
    type:\33[92;3muse port_checker\33[00m in the Pandora prompt \33[1mpan<( \33[00m
    1->type the address or ip of target
    2->type the port to check
    you can check up to five port or type `quit` 
    to exit.
    example:
    \33[93;3m<( example.com
    <( 80
       ...\33[00m
    
   """)



def subdomain_finder_help():
    print("""
    Tool Name: Subdomain Finder

    ---+Description
    It is used to check subdomains of a domain.



    ---+Usage
    type: \33[92;3muse subdomain_finder\33[00m in the Pandora prompt 
    \33[1mpan<( \33[00m
    1->type address of domain you want to find the
    subdomains.
    Hit enter then let Pandora do the rest.
    example:
    \33[93;3m<( example.com
    \33[00m
       """)

def helper(tool):
    if tool == "whois":
        whois_help()

    elif tool == "ddos":
        ddos_help()

    elif tool == "hash_cracker":
        hasher_help()

    elif tool == "subdomain_finder":
        subdomain_finder_help()

    elif tool == "port_scanner":
        port_scanner_help()

    elif tool == "port_checker":
        port_checker_help()

    elif tool == "listener":
        listener_help()

    elif tool == "page_clonner":
        page_clonner_help()

    else:
        print_warning("tool not found")