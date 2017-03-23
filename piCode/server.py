# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 05:49:34 2017

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
    
#Bind the socket
try:
    mysock.bind(("",1234)) #dont know the client ip address yet, and use any old port
except socket.error:
    print("Failed to bind")
    sys.exit()
mysock.listen(5)
while True:
    conn,addr=mysock.accept()
    data=conn.recv(1000)
    if not data:
        break
    conn.sendall(data) #echo the data riht back to the client - could process the data first
conn.close()
mysock.close()