import socket

def listensocket(): #port,
    port= 10
    backlog=5
    connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    connection.bind(('',port))
    connection.listen(backlog)
    print 'host listening on '+str(connection)
    return connection
listensocket()