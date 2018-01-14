# This code is designed to make a socket to listen  for peers trying to connect
import socket

def listensocket(): #port
    host='' #generic name
    port= 10
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
        conn,addr= connection.accept()
        print 'connected with '+ addr[0]+':'+str(addr[1])
    connection.close()

    return connection
listensocket()