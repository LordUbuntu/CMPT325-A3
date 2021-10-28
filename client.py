from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)

# get client.py server_host server_port filename
# client.py server_host server_port filename
serverName = sys.argv[1]
serverPort = int(sys.argv[2])
fileName = sys.argv[3]

# connect
clientSocket.connect((serverName,serverPort))

# send
message = "GET /" + fileName
clientSocket.send(message.encode())

# receive
htmlInfo = clientSocket.recv(1024)
print(htmlInfo.decode())

clientSocket.close()
