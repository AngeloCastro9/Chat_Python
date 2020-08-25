import socket
from datetime import datetime

host = '127.0.0.2'
sendPort = 7001
myAddress = (host, sendPort)

receivePort = 7000
otherAddress = ('127.0.0.1', receivePort)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(otherAddress)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serv_socket.bind(myAddress)

serv_socket.listen(10)
print('Waiting connection')
con, cliente = serv_socket.accept()
print('Connected')

myName = input("Your name: ")
clientSocket.send(myName.encode('utf-8'))

print("Waiting for someone else to enter name ...")
clientName = con.recv(1024).decode("utf-8")
loopMessage = True
while loopMessage:
    
    message = input("Me: ")
    clientSocket.send(message.encode('utf-8'))

    if(message == "Bye" or message == "bye"):
        print("Your connection is closed.")
        serv_socket.close()
        clientSocket.close()
        loopMessage = False
    else:
        
        print( "Waiting message..." )
        receive = con.recv(1024)
        time = datetime.now().strftime('%H:%M:%S')
        print( clientName + "at" + time + ": " + receive.decode("utf-8") )

        if receive.decode("utf-8") == "bye" or receive.decode("utf-8") == "Bye":
            print("Your connection is closed because " + clientName + " sent 'Bye'")
            serv_socket.close()
            clientSocket.close()
            loopMessage = False