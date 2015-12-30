__author__ = 'fturan'
import threading
import socket
import Queue
import time

nlsize = 50
connect_point_list={}
function_list=['convertGray','filterPrewitt','Binarize','filterSobel','filterGaussian']

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


class ServerReadThread(threading.Thread):
    def  __init__(self, name, cSocket, address, threadQueue ):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address
         self.tQueue = threadQueue

    def parser(self,data):
        if data[0:5]=="HELLO":
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
                print (str(connect_point_list.keys()[i]) + ':'+ str(connect_point_list.keys()[i+1]) + ':' +
                       str(connect_point_list.value()[i]) + ':' + str(connect_point_list.value()[i+1]))
                print "\n"
            self.cSocket.send("NLIST END\n")

        if data[0:5]=="FUNRQ":
            functionname=data[6:]
            if functionname in function_list:
                response= "FUNYS" + functionname
            else:
                response="FUNNO" +functionname

            self.cSocket.send(response)

 #       if data[0:5]=="EXERQ":

#        if data[0:5]=="PATCH":


    def run(self):
        while True:
                incoming_data = self.cSocket.recv(1024) #clienttan veri bekliyoruz.
                if incoming_data != " ":                 # eger client birsey gonderdiyse
                    print "incoming_data: " + incoming_data
                    self.parser(incoming_data)
                   # print "message: " + message
                  #  self.tQueue.put(message)      # parser'la ne demek istedigini anliyoruz, ve ona verecegimiz cevabi, kuyrugumuza yaziyoruz

        self.cSocket.close()
   
class ClientWriteThread(threading.Thread):
    def  __init__(self, name, cSocket, address, threadQueue ):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address
         self.tQueue = threadQueue

class ClientThread(threading.Thread):
     def  __init__(self, name,serverip,serverport,ip,port):
         threading.Thread.__init__(self)
         self.name=name
         self.serverip=serverip
         self.serverport=serverport
         self.ip=ip
         self.port=port
         self.sock=socket.socket()

    def run(self):
        self.sock.connect(self.serverip,self.serverport)
        ConnextionControl=ConnextionControlThread("connectioncontrolthread",self.ip,self.port)
        ConnextionControl.start()

#10 dakikada bir peer'lara burda misin kontrolü yapicaz
class ConnextionControlThread(threading.Thread):
    def  __init__(self, name,ip,port):
         threading.Thread.__init__(self)
         self.name=name
         self.ip=ip
         self.port=port

    def run(self):
         while True:
             time.sleep(600)
             for i in len(connect_point_list):
                s=socket.socket()
             s.connect(connect_point_list.keys()[i],connect_point_list.vales()[i])
             s.send("HELLO")
             data=s.recv(1024)
             if data[0]=='SALUT':
                if data[1]=="P":
                     connect_point_list[self.ip,self.port]=("P",time,"S")

                if data[1]=="N":
                  connect_point_list[self.ip,self.port]=("N",time,"S")

             s.send("CLOSE")
             if data[0]=="BUBYE":
                         s.close()

serverThread=ServerThread()
serverThread.start()
    
