#!/usr/bin/python

import socket

# the public network interface
#HOST = socket.gethostbynameo(socket.gethostname())
# ipaddrlist=[172.27.27.0-254]
for i in range(1,254):
    #Should not stop if unknown host??
    try:
        HOST = socket.gethostbyaddr('172.27.27.' +str(i))
        print (HOST)
    except:
        pass
