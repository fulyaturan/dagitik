__author__ = 'fturan'
import threading
import socket
import Queue
import time

connect_point_list={}
connect_point={}
class ServerReadThread(threading.Thread):
    def  __init__(self, name, cSocket, address):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address
         #self.ip=address[0]
         #self.port=port
         #self.tQueue = threadQueue

    def parser(self,data):

        data=data.strip()

        if data[0:5]=='HELLO':

            response='SALUT' + str('N')
            self.cSocket.send(response)

        if data[0:5]=='CLOSE':
            self.cSocket.send('BUBYE')
            self.cSocket.close()

        if data[0:5]=='REGME':
            data1=data[6:].split(":")
            currentTime=time.time()
            ip=data1[0]
            port=data1[1]
            self.ip=ip
            self.port=port
            connect_point={ip:port}

            if connect_point_list.has_key(ip,port):
                response='REGOK'+str(currentTime)
                self.cSocket.send(response)

            else :
                response='REGWA'
                connect_point_list[(connect_point)]='W',str(currentTime)
                print connect_point_list
                self.cSocket.send(response)

        if data[0:5]=='GETNL':




    def run(self):

        while True:
                incoming_data = self.cSocket.recv(2048) #clienttan veri bekliyoruz.
                if incoming_data != "":                 # eger client birsey gonderdiyse
                    print "incoming_data: " + incoming_data
                    message = self.parser(incoming_data)
                    print "message: " + message
                  #  self.tQueue.put(message)      # parser'la ne demek istedigini anliyoruz, ve ona verecegimiz cevabi, kuyrugumuza yaziyoruz
                  
        self.cSocket.close()


class ClientThread(threading.Thread):
    def  __init__(self, name, cSocket, address, threadQueue ):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address

         self.tQueue = threadQueue

    def cparser(self,data):
         data=data.strip()

        

    def run(self):
        port = 12345
        s.connect(('', port))


port=12345
threadQueue=Queue.Queue()
s = socket.socket()
st = ServerThread("ServerThread", s,port ,threadQueue)
st.start()
ct = ClientThread("ClientThread", s, threadQueue)
ct.start()
