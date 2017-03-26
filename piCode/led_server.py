# -*- coding: utf-8 -*-
"""
try a simple server to turn led on/off
Created on Thu Mar 23 05:49:34 2017
@author: mbh
"""

import socket
import sys
import Rpi.GPIO as GPIO

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
#listen for a request
mysock.listen(5)
while True:
    #accept request
    conn,addr=mysock.accept()
    #receive the data
    data=conn.recv(1000)
    if not data:
        break
    if data == b'on':
        GPIO.output(13,True)
    if data == b'off':
        GPIO.output(13,False)       
    #send a response (in this case just an echo)
    conn.sendall(data) #echo the data riht back to the client - could process the data first
conn.close()
mysock.close()