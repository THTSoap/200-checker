#Coded By Soap
import requests
from colorama import *
from multiprocessing.dummy import Pool

init(autoreset=True)

print("""
\033[91m\tWeb Site 200 Checker
\033[92m\tTelegram: @captainsoap1
\033[92m\tDiscord: 'Captain Soap#8404
""")

def statuscheck(url):
    try:
        website = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36:url"})
        if website.status_code == 200:
            print(Fore.GREEN + url + '---> Site Ayakta!')
            open('siteler.txt', 'a').write(url + '\n')
        else:
            print(Fore.RED + url + ' ---> Site Calismiyor')
    except:
        pass

def list():
    try:
        txtpath = input('\033[96mTxt Yolunu Belirtiniz: ')
        try:
            with open(txtpath, 'r') as (get):
                read = get.read().splitlines()
        except IOError:
            pass

        read = txtpath(read)
        try:
            xx = Pool(1)
            xx = xx.map(statuscheck, read)
        except:
            pass
    except:
        pass
list()