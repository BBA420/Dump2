import os,time
os.system('clear')
os.system('xdg-open https://facebook.com/MUB4SH4R/');time.sleep(2)
from platform import uname
arch=uname().machine.lower()
if 'aarch' in arch:
    os.system('chmod 777 baloch && ./baloch')
else:
    print(' \033[1;35m Your device not support');exit()
