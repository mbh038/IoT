# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:50:30 2017

@author: mbh
"""

import socket
import time

ms=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ms.connect(('192.168.1.95',1234))

def speak():
    while True:
        ms.sendall(b'on')
        time.sleep(1)
        ms.sendall(b'off')
        time.sleep(1)
    
    
if __name__ == "__main__":
    try:
        speak()
    except KeyboardInterrupt:
        ms.close()
    