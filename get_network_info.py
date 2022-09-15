import sys
import os
import subprocess as s

with open('info.txt','w') as f:
    if os.name == 'nt':
        print('Windows')
        #p = s.Popen(['netsh', 'wlan show networks'], stdout = f)
        p = s.Popen([r'c:\windows\system32\dir','*.*'], stdout = f)
    elif os.name == 'posix':
        print('Linux')
    else:
        print('other')