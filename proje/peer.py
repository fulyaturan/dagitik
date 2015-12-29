__author__ = 'fturan'
import threading
import socket
import Queue
import time

nlsize = 50
connect_point_list={}
function_list=['convertGray','filterPrewitt','Binarize','filterSobel','filterGaussian']

class ServerThread(threading.Thread):
    def  __init__(self, name, cSocket, address, threadQueue ):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address
         self.tQueue = threadQueue


    def run(self):


class ServerReadThread(threading.Thread):
    def  __init__(self, name, cSocket, address, threadQueue ):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address
         self.tQueue = threadQueue

    def parser(self,data):
        
    def run(self):    
class ClientWriteThread(threading.Thread):
    def  __init__(self, name, cSocket, address, threadQueue ):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address
         self.tQueue = threadQueue

class ClientReadThread(threading.Thread):
    def  __init__(self, name, cSocket, address, threadQueue ):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address
         self.tQueue = threadQueue
        
    def parser(self,data):
class ClientThread(threading.Thread):
    def  __init__(self, name, cSocket, address, threadQueue ):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address
         self.tQueue = threadQueue


    def run(self):
    
