from socket import *
import json
from datetime import datetime

serverPort = 8000
while True:
    fileInput = input("Enter file name ")
    requestedFile = fileInput.split('.')[0]

    contentFile = open("contents.txt",'r')

    lookupJson = contentFile.read()
    contentFile.close()

    lookupDictionary = json.loads(lookupJson)
    count = 0
    for i in range(1,6):
        chunk = requestedFile + '_' + str(i)
        isChunkDownloaded = False
        for userIP in lookupDictionary[chunk]:
            clientSocket = socket(AF_INET, SOCK_STREAM)
            try:
                clientSocket.connect((userIP,serverPort))
                request = {
                    "requested_content": chunk
                }
                requestJson = json.dumps(request)

                clientSocket.send(requestJson.encode())
                print("request sended")
                with open("downloaded_" +requestedFile+"_"+str(i), "wb") as f:
                    count += 1
                    while True:
                        bytes_read = clientSocket.recv(4096)
                        # print(len(bytes_read))
                        if len(bytes_read) <= 0:
                            break
                        f.write(bytes_read)
                        isChunkDownloaded = True
            except:
                clientSocket.close()
                continue
            
        if not isChunkDownloaded:
            print(f"CHUNK {chunk} CANNOT BE DOWNLOADED FROM ONLINE PEERS.")
            continue

        if(isChunkDownloaded):
            now = datetime.now()
            current_time = now.strftime("%d/%m/%Y %H:%M:%S")

            with open("download_log.txt","a") as file:
                file.write(f"chunk {chunk} downloaded from {userIP} at {current_time} \n")
        else:
            print(f"failed to download chunk {chunk}")


        clientSocket.close()


    if count == 5:
        content_name = "downloaded_" +requestedFile  # again, this'll be the name of the content that used wanted to download from the network.
        chunknames = [content_name+'_1', content_name+'_2', content_name+'_3', content_name+'_4', content_name+'_5']
        print(chunknames)
        #with open(content_name+'.png', 'w') as outfile: 
        with open('hello.png', 'wb') as outfile: # in your code change 'ece.png' to content_name+'.png'
            for chunk in chunknames: 
                with open(chunk, 'rb') as infile: 
                    outfile.write(infile.read() )
                infile.close()
        print("file is successfully downloaded")





