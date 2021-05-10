from socket import *
import json
from datetime import datetime


serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)



while True:
    print('The server is ready to receive')

    connection , (addr,port) = serverSocket.accept()
    print(f"connection from {addr} has been established")
    requestJson =  connection.recv(4096).decode()
    print("requiest received")

    requestedFile = json.loads(requestJson)

    filename = requestedFile['requested_content']

    with open(filename,'rb') as file:
        connection.sendall(file.read())
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    with open("upload_log.txt","a") as file:
        file.write(f"chunk {filename} sended to {addr} at {current_time} \n")

    connection.close()


print("file sended")

        




