__author__ = 'fturan'
import threading
import socket
import Queue
import time

connect_point_list={}
connect_point={}
class ServerThread(threading.Thread):
    def  __init__(self):
         threading.Thread.__init__(self)
         self.cSocket = socket.socket()
         self.ip = '127.0.0.1'
         self.port=12345
         self.cSocket.bind((self.ip,self.port))
         self.cSocket.listen(4)

    def run(self):
        print 'burasi benim baglanti bekledigim yer'
        while True:

            c,addr=self.cSocket.accept()
            readThread=ServerReadThread("serverreadthread",c,addr)
            print 'Got connection from', addr
            readThread.start()
            #name,serverip,serverport,ip,port
            clientThread=ClientThread("clientThread",self.ip,self.port,c,addr)
            clientThread.start()
            
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
            print "parserda HELLO if'ine girdi."
            response='SALUT' + str('N')
            self.cSocket.send(response)

        if data[0:5]=='CLOSE':
            self.cSocket.send('BUBYE')
            self.cSocket.close()
            if self.ip in connect_point_list.keys():
                del connect_point_list[self.ip]

        if data[0:5]=='REGME':
            data1=data[6:].split(":")
            currentTime=time.time()
            ip=data1[0]
            port=data1[1]
            self.ip=ip
            self.port=port
            connect_point={'ip':'port'}

            if connect_point_list.has_key(ip,port):
                response='REGOK'+str(currentTime)
                self.cSocket.send(response)

            else :
                response='REGWA'
                connect_point_list[(connect_point)]=('W',str(currentTime))
                print connect_point_list
                self.cSocket.send(response)

        if data[0:5]=='GETNL':
            nlsize=int(data[6:])
            self.cSocket.send("NLIST BEGIN\n")
            for i,j in len(connect_point_list):
                print str(connect_point_list.keys()[i]) + ':'+ str(connect_point_list.keys()[i+1]) + ':' + str(connect_point_list.value()[i]) + ':' + str(connect_point_list.value()[i+1]) 
                print "\n"
            self.cSocket.send("NLIST END\n")


    def run(self):

        while True:
                incoming_data = self.cSocket.recv(2048) #clienttan veri bekliyoruz.
                if incoming_data != "":                 # eger client birsey gonderdiyse
                    print "incoming_data: " + incoming_data
                    message = self.parser(incoming_data)
                    print "message: " + message
                  #  self.tQueue.put(message)      # parser'la ne demek istedigini anliyoruz, ve ona verecegimiz cevabi, kuyrugumuza yaziyoruz
                  
        self.cSocket.close()

class ClientReadThread(threading.Thread)
    def  __init__(self, name,serverip,serverport,ip,port):
         threading.Thread.__init__(self)
         self.name=name
         self.serverip=serverip
         self.serverport=serverport
         self.ip=ip
         self.port=port
         self.s=socket.socket()

    def cparserecv(self,data):
         data=data.stlip(" ")

         if data[0]=='SALUT':
             if data[1]=="P":
                 connect_point_list[self.cSocket,self.address]=("P",time,"S")

             if data[1]=="N":
                  connect_point_list[self.cSocket,self.address]=("N",time,"S")

         if data[0]=="BUBYE":
             self.cSocket.close()

   # def cparsersend(self,data):
    #    data=data.strip()

    def run(self):
        print "ip: " + str(self.ip) + " - port: " + str(self.port)
        receivedata=self.s.recv(2048)
        if receivedata != "":
                 print "incoming_data: " + receivedata
                 cmessage = self.cparserecv(receivedata)
                 print "message: " + cmessage

class ClientThread(threading.Thread):
    def  __init__(self, name, cSocket, address ):
         threading.Thread.__init__(self)
           threading.Thread.__init__(self)
         self.name=name
         self.serverip=serverip
         self.serverport=serverport
         self.ip=ip
         self.port=port
         self.sock=socket.socket()


    def run(self):
        self.sock.connect(self.serverip,self.serverport)
        clientreadthread=ClientReadThread("clientreadthread",self.ip,self.port,self.serverip,self.serverport,self.sock)
        clientreadthread.start()
        

st = ServerThread()
st.start()
#ct = ClientThread("ClientThread", s, threadQueue)
#ct.start()
