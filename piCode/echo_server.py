# -*- coding: utf-8 -*-
"""

# Example of simple echo server
# www.solusipse.net

Created on Sun Mar 26 10:34:05 2017
@author: mbh
"""

import socket
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('', 1234))
    connection.listen(10)
    while True:
        current_connection, address = connection.accept()
        while True:
            data = current_connection.recv(2048)

            if data == 'quit\r\n':
                current_connection.shutdown(1)
                current_connection.close()
                break

            elif data == 'stop\r\n':
                current_connection.shutdown(1)
                current_connection.close()
                exit()

            elif data:
                if data == b'on':
                    GPIO.output(13,True)
                if data == b'off':
                    GPIO.output(13,False)   
                current_connection.send(data)
                print (data)


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
