__author__ = 'fturan'

import socket
import threading

s = socket.socket()
host =socket.gethostname()
port = 12345
s.connect((host, port))

while True:
    s.send('heeey')
    message=s.recv(1024)
    print message

s.close()
