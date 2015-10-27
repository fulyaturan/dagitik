__author__ = 'fturan'

import socket
import threading

s = socket.socket()
host =socket.gethostname()
port = 12345
s.connect((host, port))

s.send('heeey')

s.close()
