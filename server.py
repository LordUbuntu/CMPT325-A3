# import socket module
from socket import *
import sys  # In order to terminate the program


serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  # Fill in start #Fill in end
    try:
        message =  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =  # Fill in start #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        # we assume that HTTP 1.1 is ubiquitous
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n")
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
        serverSocket.close()
        # Terminate the program after sending the corresponding data
        sys.exit()
