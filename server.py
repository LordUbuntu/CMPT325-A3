# import socket module
from socket import *
import sys  # In order to terminate the program


serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket

# Fill in start
serverSocket.bind(("127.0.0.1", 8182))
# this gives us only 1 possible connection, hence '1'
serverSocket.listen(1)
while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        # recieving file in packets of size 1024
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        # basic file work
        fileData = f.read()
        print(fileData)
        f.close()  # Fill in start #Fill in end
        # Send one HTTP header line into socket
        # OK header
        connectionSocket.send("HTTP/1.0 200 OK\r\n")
        # once we have read the file and closed it we can
        # Send the content of the requested file to the client
        for i in range(0, len(fileData)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        # we assume that HTTP 1.1 is ubiquitous
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
        serverSocket.close()
        # Terminate the program after sending the corresponding data
    sys.exit()
