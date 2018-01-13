#code to get ip address of the local host
import socket

def getip():
    connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #create socket to communicate with IPv4 and TCP
    connection.connect(('www.google.com', 80)) #ping google at port 80
    ip= connection.getsockname()[0] # gives IP address and port of the local host . [0] returns only ip address
    print ip
    return ip
getip()