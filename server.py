# import socket module
from socket import *
import sys  # In order to terminate the program


serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket

# Fill in start
## this is the ip of the TWU guest wifi on my computer, to run from your own computer find the IP of the network you are on and make that the first dimension of the tuple
serverSocket.bind(("10.18.3.60", 8182))
# this gives us only 1 possible connection, hence '1'
serverSocket.listen(5)
while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        # recieving file in packets of size 1024
        message = connectionSocket.recv(1024)
        filename = message.split()[1]

        # read html file into `fileData` if it exists
        f = open(filename[1:])
        fileData = f.read()
        f.close()

        # Send HTTP header
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-type:text/html\r\n".encode())

        # once we have read the file and closed it we can
        # Send the content of the requested file to the client
        # (alternatively sendall(fileData.encode()) can replace the for loop)
        for i in range(0, len(fileData)):
            connectionSocket.send(fileData[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        # we assume that HTTP 1.1 is ubiquitous
        connectionSocket.send("HTTP/1.1 404 NOT FOUND\n\nFILE NOT FOUND\r\n".encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
serverSocket.close()
sys.exit()
