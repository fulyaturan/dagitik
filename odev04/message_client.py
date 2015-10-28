__author__ = 'fturan'

import socket
import threading

class readThread (threading.Thread):
    def __init__(self, sa):
        threading.Thread.__init__(self)
        self.sa = sa
    def run(self):
        while True:
            message = self.sa.recv(1024)
            print message
        self.sa.close()
    print 'bbb'


class writeThread (threading.Thread):
    def __init__(self, sa):
        threading.Thread.__init__(self)
        self.sa = sa
    def run(self):
        while True:
            konsol=raw_input()
            self.sa.send(konsol)
        self.sa.close()


s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))


rThread = readThread(s)
rThread.start()
wThread = writeThread(s)
wThread.start()
