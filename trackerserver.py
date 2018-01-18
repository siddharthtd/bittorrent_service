# This code is designed to make a socket to listen  for peers trying to connect.
#the server connects to the peer, receives file from peer and save it at the given location
import socket
import os
from threading import Thread
from SocketServer import ThreadingMixIn

class ServerThread(Thread):
    def __init__(self,ip,port):

def listensocket(): #port
    host=socket.gethostname() #gethostname
    port= 8883

    backlog=10 #Number of requests to be queued
    connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating a socket that communicates with IPv4 protocol and TCP
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #setting socket option: value 1 to make the port reuasabe after every 1 exit.
    try:                                                                #this prevents the port already use error
        connection.bind((host,port))  #bind port to receive connections
    except socket.error as msg:
        print' bind failed: '
    else: print' bind successfull'

    connection.listen(backlog) #start listening for queus ranging till backlog=5
    print' server listening'
    print 'host listening on '+str(connection)
    while 1:
        conn,(ipaddr,portnum)= connection.accept()
        print 'connected with '+ ipaddr+':'+str(portnum)
        receivefile(conn)
    connection.close()



def receivefile(sockdata):
    filename= 'filename'+'.zip'
    path= 'C:\Users\Deepak\PycharmProjects\bittorrent_service\Testfiles\serverdb'
    filepath = os.path.join(path, filename)
    outputfile=open(filename,'wb')

    while True:
        data=sockdata.recv(1023) #buffer size receive
        print 'data received'
        if not data: break
        outputfile.write(data)
    outputfile.close()
    print'done receiving'
    return

listensocket()