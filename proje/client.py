#deneme amacli basit bir client

import socket

s = socket.socket()

print "CLIENT: baglanacak"
s.connect(("127.0.0.1", 12345))
print "CLIENT: baglanti kuruldu"

s.send("HELLO")

while True:
    a = s.recv(1024)
    if (a != ""):
        print "recv: " + a
