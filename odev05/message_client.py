__author__ = 'fturan'
import sys
import socket
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import*
import Queue
import time

class ReadThread (threading.Thread):
    def __init__(self, name, csoc, threadQueue, app):
        threading.Thread.__init__(self)
        self.name = name
        self.csoc = csoc
        self.nickname = " "
        self.threadQueue = threadQueue
        self.app = app

    def incoming_parser(self, data):
        if len(data) == 0:
            return

        if len(data) > 3 and not data[3] == " ":
            response = "ERR"
            self.csoc.send(response)
            return
        rest = data[4:]

        if data[0:3] == "BYE":
            self.app.cprint("bye bye!" +rest)

        if data[0:3] == "HEL":
            self.app.cprint("welcome" +rest)

        if data[0:3] == "ERL":
            self.app.cprint("register first" +rest)

        if data[0:3] == "REJ":
            self.app.cprint("rejected" +rest)

        if data[0:3] == "MNO":
            self.app.cprint("there isn't this user" +rest)


        if data[0:3] == "MOK":
            self.app.cprint("message send succes" +rest)

        if data[0:3] == "SOK":
            self.app.cprint("message send succes" +rest)


        if data[0:3] == "LSA":
            splitted = rest.split(":")
            msg = "-Server- Registered nicks: "
            for i in splitted:
                msg += i + ","
            msg = msg[:-1]

            self.app.cprint(msg)

    def run(self) :
        while True:
            data = self.csoc.recv(1024)

class WriteThread (threading.Thread):
    def __init__(self, name, csoc, threadQueue):
        threading.Thread.__init__(self)
        self.name = name
        self.csoc = csoc
        self.threadQueue = threadQueue

    def run(self):

        if self.threadQueue.qsize() > 0:
            queue_message = self.threadQueue.get()

            try:
                self.csoc.send(queue_message)
            except socket.error:
                self.csoc.close()
                break

class ClientDialog(QDialog):
    def __init__(self, threadQueue):
        self.threadQueue = threadQueue

         #create a Qt application --- every PyQt app needs one
        self.qt_app = QApplication(sys.argv)
        # Call the parent constructor on the current
        QDialog.__init__(self, None)

        # Set up the window
        self.setWindowTitle('IRC Client')
        self.setMinimumSize(500, 200)

        self.vbox = QVBoxLayout()

        self.sender = QLineEdit("", self)

        self.channel = QTextBrowser()

        self.send_button = QPushButton('&Send')

        self.send_button.clicked.connect(self.outgoing_parser)

        # Add the controls to the vertical layout
        self.vbox.addWidget(self.channel)
        self.vbox.addWidget(self.sender)
        self.vbox.addWidget(self.send_button)
        # A very stretchy spacer to force the button to the bottom
        # self.vbox.addStretch(100)
        # Use the vertical layout for the current window
        self.setLayout(self.vbox)
    def cprint(self, data):
        self.channel.append(data)

    def outgoing_parser(self):
        data = self.sender.text()
        if len(data) == 0:
            return
        if data[0]=="/":
            command=data[1:5]
            if command==list:
                self.threadQueue.put("LSQ")
            if command=="quit":
                self.threadQueue.put("QUI")
            if command=="nick":
                self.threadQueue.put("USR")
            if command=="msg":
                message=data.split(" ")
                nickname=message[0]
                msg=message[1]
                self.threadQueue.put("MSG" +nickname +msg)
    def run(self) :
        self.show()
        self.qt_app.exec_()

s = socket.socket()
host = socket.gethostname() # Get local machine name
port = 12345
s.connect((host, port))

sendQueue =Queue.Queue
app = ClientDialog(sendQueue)

rt = ReadThread("ReadThread", s, sendQueue, app)
rt.start()
wr = WriteThread("WriteThread", s, sendQueue, app)
wr.start()
