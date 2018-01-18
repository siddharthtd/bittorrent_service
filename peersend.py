#Sending a file to server at given local host port
import socket
import os


def listenport():
    s=socket.socket()
    host=socket.gethostname()
    port=8883

    s.connect((host,port)) #connect to the host
    filename='Documents'+'.zip'
    path=r'C:\Users\Deepak\PycharmProjects\bittorrent_service\Testfiles'
    filepath=os.path.join(path,filename)
    f= open(filepath,'rb')
    l=f.read(1023)
    #till reading, read and send l sized data
    while (l):
        try:
            s.send(l)
            print ('Sent',repr(l))
            l=f.read(1023)
        except KeyboardInterrupt:
            print' interruppted'
    f.close()
    print 'done sending'
listenport()


