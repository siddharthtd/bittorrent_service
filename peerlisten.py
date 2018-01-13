# This code is designed to make a socket to listen  for peers trying to connect
import socket

def listensocket(): #port
    port= 10
    backlog=5 #Number of requests to be queued
    connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating a socket that communicates with IPv4 protocol and TCP
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #setting socket option: value 1 to make the port reuasabe after every 1 exit.
                                                                    #this prevents the port already use error
    connection.bind(('',port))  #bind port to receive connections
    connection.listen(backlog) #start listening for ques ranging till backlog=5
    print 'host listening on '+str(connection)
    return connection
listensocket()