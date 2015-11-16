__author__ = 'fturan'
import threading
import socket
import Queue
import time
fihrist={}

class LoggerThread (threading.Thread):
    def __init__(self, name, logQueue, fid):
            threading.Thread.__init__(self)
            self.name = name
            self.lQueue = logQueue
# dosyayi appendable olarak ac
            self.fid =open("log.txt","a")

    def log(self,message):
# gelen mesaji zamanla beraber bastir
        t = time.ctime()
        self.fid.write(t + message )
        self.fid.flush()
    def run(self):
        self.log("Starting " + self.name)

        while True:

            # lQueue'da yeni mesaj varsa
            # self.log() methodunu cagir
            if not lQueue.empty():
                to_be_logged = self.lQueue.get()
                self.log(to_be_logged)

        self.log("Exiting" + self.name)
        self.fid.close()
        
        
class WriteThread(threading.Thread):
    def  __init__(self, name, cSocket, address, threadQueue, logQueue ):
         threading.Thread.__init__(self)
         self.name = name
         self.cSocket = cSocket
         self.address = address
         self.lQueue = logQueue
         self.tQueue = threadQueue

    def run(self):
        self.lQueue.put("Starting" + self.name)
        while True:


            if self.threadQueue.qsize() > 0:
                queue_message = self.threadQueue.get()

                if queue_message[0:3]=="MSG":

                    message_to_send = "MSG " + queue_message[4:]


                elif queue_message[0:3]=="SAY":
                    message_to_send = "SAY " + queue_message[4:]

                else:
                    message_to_send = "SYS "

            self.cSocket.send(message_to_send)

        self.lQueue.put("Exiting"  + self.name)
        

class ReadThread (threading.Thread):

    def __init__(self,name,cSocket, address, threadQueue):
        threading.Thread.__init__(self)
        self.name = name
        self.cSocket = cSocket
        self.address = address
       # self.lQueue = logQueue
       # self.fihrist = fihrist
        self.tQueue = threadQueue

    def parser(self, data):
        data = data.strip()
        #henuz login olmadiysa
        if not self.name and not data[0:3] == "USR":
            response="oncelikle login olun"
            self.csend(response)
        #data sekli bozuksa
        #if
         #   response = "ERR"
         #   self.csend(response)
         #   return 0

        if data[0:3] == "USR":
            nickname = data[4:]
            if not fihrist.has_key(nickname):
                #kullanici yoksa
                response = "HEL" + nickname
                fihrist[self.nickname]=clientQueue
                # fihristi guncelle
                self.fihrist.update(nickname,clientQueue)
                self.lQueue.put(self.nickname + " has joined.")
                return 0
            else:
                # kullanici reddedilecek
                response = "REJ " + nickname
                self.csend(response)
                # baglantiyi kapat
                self.csoc.close()
                return 1
        elif data[0:3] == "QUI":
            response = "BYE " + self.name
            # fihristten sil
            del fihrist[self.name]
            # log gonder
            # baglantiyi sil
            self.csoc.close()
        elif data[0:3] == "LSQ":
            list = " "
            for nick in fihrist:
                list += nick + ":"
            response = "LSA " + list
        elif data[0:3] == "TIC":
            response = "TOC"
            #self.csend(response)
        elif data[0:3] == "SAY":
            message = data[4:]
            print message
            for nick in fihrist:
                if nick != self.nickname:
                    self.threadQueue.put(('SAY' +message))
                    
            self.cSocket.send("SOK")        
            
        elif data[0:3] == "MSG":
            if not to_nickname in self.fihrist.keys():
                response = "MNO"
            else :
                
                queue_message = (to_nickname, self.nickname, message)
                # gonderilecek threadQueueyu fihristten alip icine yaz
                self.fihrist[to_nickname].put(queue_message)
                response = "MOK"
            self.csend(response)
        else:
             # bir seye uymadiysa protokol hatasi verilecek
            response = "ERR"
        return response

    def run(self):
    #    self.lQueue.put("Starting " + self.name)
          #  while True:
                # burasi blocking bir recv halinde duracak
                # gelen protokol komutlari parserdan gecirilip
                # ilgili hareketler yapilacak

               # incoming_data=s.recv(2048)
               # queue_message =self.parser(incoming_data)

                # ***** SON EKLENEN ******
        while True:
                incoming_data = self.cSocket.recv(2048) #clienttan veri bekliyoruz.
                if incoming_data != "":                 # eger client birsey gonderdiyse
                    print "incoming_data: " + incoming_data
                    message = self.parser(incoming_data)
                    print "message: " + message
                    self.tQueue.put(message)      # parser'la ne demek istedigini anliyoruz, ve ona verecegimiz cevabi, kuyrugumuza yaziyoruz
        self.cSocket.close()
        # istemciye cevap hazirla
        # threadQueue'ya yaz
        # lock mekanizmasini unutma
            #self.lQueue.put("Exiting " + self.name)

threadCounter=0
s = socket.socket()
host =socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    clientQueue=Queue.Queue()
    threadCounter += 1
    rthread = ReadThread(threadCounter, c, addr, clientQueue)
    rthread.start()
