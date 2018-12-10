import requests
from bs4 import BeautifulSoup
import time
from tools.status import *

def download(link):

    filename = link.split('/')[-1]

    print_status("downloading {}".format(filename))

    try:

        r = requests.get(link, stream=True)
        
        with open('saves/' + filename, "wb") as f:
            for chunk in r.iter_content(chunk_size = 1024 * 1024):
                if chunk:
                    f.write(chunk)
    except:
        print_warning('could not download')

    print_msg("{} downloaded to /saves/{}".format(filename, filename))


def find_links(url):
    exts = ["pdf", "apk", "txt", "iso", "exe",
           "png", "jpg", "mp3", "mp4", "doc", "py"]

    tags = ["a", "img", "video", "audio", "link"]
    linkss = []
    count = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    for tag in tags:
        links = soup.findAll(tag)
        try:
            for link in links:
                for ext in exts:
                    if link['src'].endswith(ext):
                        count += 1
                        if link['src'].startswith('https://'):
                            linkss.append(link['src'])
                        else:
                            linkss.append(url + link['src'])

        except:
            for link in links:
                for ext in exts:
                    if link['href'].endswith(ext):
                        count += 1
                        if link['href'].startswith('https://'):
                            linkss.append(link['href'])
                        else:
                            linkss.append(url + link['href'])
    if len(linkss) != 0:
        cu = 1
        print_msg("found {} downloadable files".format(count))
        print_status("listing.....")
        for i in linkss:
            print_status(str(cu) +  i)
            time.sleep(0.1)
            cu += 1
    else:
        print_warning("no files found")
    return linkss

def starter():
    using = "\33[91musing\33[00m(\33[94mfile_downloader\33[00m) "
    url = input(using + 'url<( ')
    try:
        links = find_links(url)
    except:
        print_warning("invalid url")
    while len(links) != 0:
        dowl = input('command<( ')
        dowl = dowl.split()
        if len(dowl) == 1:
            if dowl[0] == "exit":
                print_status("exiting...")
                time.sleep(1)
                break
            elif dowl[0] == "list":
                for i in links:
                    print_status(i)
            else:
                print_warning("unknown command")
    
        elif len(dowl) == 2:
            if dowl[0] == "all":
                for link in links:
                    if link.endswith(dowl[1]):
                        download(link)

            elif dowl[0] == "download":
                try:
                    download(links[int(dowl[1]) - 1])
                except:
                    print_error('doesnt exist')

            else:
                print_warning("unknown command")
        else:
            print_status("unknown command")

        
