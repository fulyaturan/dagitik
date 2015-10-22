__author__ = 'fturan'

import Queue
import threading
import time
alfabe='abcdefghijklmnopqrstuvwxyz'

shift = int(raw_input("What is your shift? "))
n = int(raw_input("What is your thread number? "))
l = int(raw_input("blok uzunlugu? "))

sifrelist= Queue.Queue()
cipherlist= Queue.Queue()

f =open("metin.txt","r")
plaintext=f.read()
i = 0
while i  < len(plaintext):
    sifrelist.put(plaintext[i:i+l])
    i += l


def sifrele():
    j = 0
    while j < sifrelist.qsize():
        cipher = ''
        word = sifrelist.get()
        for i in word:
            try:
                i = (alfabe.index(i) - shift) % 26
                cipher += alfabe[i]
            except ValueError:
                cipher += i
        cipherlist.put(cipher)
        print cipher
    return cipher.upper()

cipher = sifrele()


f.close()

f=open("crypted.txt","a")
f.write(cipher)
f.close()


exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"







