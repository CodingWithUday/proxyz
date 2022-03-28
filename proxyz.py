import requests
from colorama import *
import os 
import time
import random

hehe = "SUBSCRIBE TO CODING WITH UDAY"

init(convert=True)

os.system('cls' if os.name == 'nt' else 'clear')

# FILES

https_file = open("https.txt","a") 
socks4_file = open("socks4.txt", "a")
http_file = open("http.txt", "a")
socks5_file = open("socks5.txt", "a")


# REQUEST API

rhttps = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&country=ALL&anonymity=elite&ssl=no')
rhttp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&country=ALL&anonymity=elite&ssl=no')
rs4 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks4')
rs5 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks5')


# HTTPS

https = []
https = rhttps.text
https = https.split()
lines = len(https)


# HTTP

http = []
http = rhttp.text
http = http.split()
hlines = len(http)


# SOCKS 4

socks4 = []
socks4 = rs4.text
socks4 = socks4.split()
slines = len(socks4)

# SOCKS 5

socks5 = []
socks5 = rs5.text
socks5 = socks5.split()
sslines = len(socks5)


number = random.randint(1, 5)

def getsocks4():
    for i in range(number):
        print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTCYAN_EX + "HTTPS" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTGREEN_EX + https[number])
        time.sleep(0.1)




def getsocks5():
    for b in range(number):
        print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTMAGENTA_EX + "SOCKS5" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTGREEN_EX + socks5[number])
        time.sleep(0.1)



def main():
    print(Fore.LIGHTRED_EX + '''
 _______   _______    ______   __    __  __      __  ________ 
|       \ |       \  /      \ |  \  |  \|  \    /  \|        \ 
| $$$$$$$\| $$$$$$$\|  $$$$$$\| $$  | $$ \$$\  /  $$ \$$$$$$$$
| $$__/ $$| $$__| $$| $$  | $$ \$$\/  $$  \$$\/  $$     /  $$ 
| $$    $$| $$    $$| $$  | $$  >$$  $$    \$$  $$     /  $$  
| $$$$$$$ | $$$$$$$\| $$  | $$ /  $$$$\     \$$$$     /  $$   
| $$      | $$  | $$| $$__/ $$|  $$ \$$\    | $$     /  $$___ 
| $$      | $$  | $$ \$$    $$| $$  | $$    | $$    |  $$    \ 
 \$$       \$$   \$$  \$$$$$$  \$$   \$$     \$$     \$$$$$$$$ - V2

              Note - Use At Your Own Risk. The Developer Of This Software Will Not 
              Be Hold Liable For Any Bad Activities You Do!
                                                              
                 MADE BY - Coding With Uday
                 Website - https://codeuday.rf.gd
                 YouTube - https://youtube.com/codingwithuday
                 Github  - https://github.com/CodingWithUday     
''')
    time.sleep(3)
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "1" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTWHITE_EX + "HTTPS")
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "2" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTWHITE_EX + "HTTP")
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "3" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTWHITE_EX + "SOCKS4")
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "4" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTWHITE_EX + "SOCKS5")
    print(Fore.RESET + ' ')
    a = input(Fore.LIGHTWHITE_EX + "Choose Type of Proxy : ")
    if(a == "1"):
        for i in range(lines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX + "Success -> HTTPS" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTRED_EX + https[i])
            https_file.write('\n' + https[i])
            time.sleep(0.1)
    elif(a == "2"):
        for a in range(hlines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX + "Success -> HTTP" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTRED_EX + http[a])
            http_file.write('\n' + http[a])
            time.sleep(0.1)
    elif(a == "3"):
        for b in range(slines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX + "Success -> SOCKS4" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTRED_EX + socks4[b])
            socks4_file.write('\n' + socks4[b])
            time.sleep(0.1)
    elif(a == "4"):
        for c in range(sslines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTGREEN_EX + "Success -> SOCKS5" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTGREEN_EX + socks5[c])
            socks5_file.write('\n' + socks5[c])
            time.sleep(0.1)
    else:
        print(f"No Option Found Named -> '{a}' ")









if __name__ == "__main__":

    main()
    print("All Proxy's Successfully Generated And Saved To File!")

os.system('pause' if os.name == 'nt' else 'pause')









print('SUBSCRIBE CODING WITH UDAY')
