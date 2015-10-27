__author__ = 'fturan'

import threading
import socket
import random
import time

threadCounter=0

class  myThread (threading.Thread):
    def __init__(self, threadID, clientSocket, clientAddr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.clientSocket = clientSocket
        self.clientAddr = clientAddr
    def run(self):
        print"Starting Thread-" +str(self.threadID)

        while True:
            data=c.recv(1024)
            if data=='':
               print('olmaz')
            else:
                c.send('peki' +str(addr))


        print "Ending Thread-" +str(self.threadID)


s = socket.socket()
host =socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    print "Waiting for connection"
    c, addr = s.accept()
    print'Got a connection from', addr
    threadCounter += 1
    thread = myThread(threadCounter, c, addr)
    thread.start()
