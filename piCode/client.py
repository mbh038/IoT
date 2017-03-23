# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:23:54 2017

@author: mbh
"""

import socket
import sys

#Create socket
try:
    mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    sys.exit()
try:
    host=socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("Failed to get host")
    sys.exit()
#Establish TCP session via IP address and port specified
mysock.connect((host,80))
message= "GET / HTTP/1.1\r\n\r\n"
try:
    mysock.sendall(message.encode('utf-8'))
except socket.error:
    print("Failed to send")
    sys.exit()
data=mysock.recv(1000)
print(data)
mysock.close()
        
    
    