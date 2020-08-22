import socket
from datetime import datetime

host = '127.0.0.1'
receivePort = 7000

myAddress = (host, receivePort)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(myAddress)

serv_socket.listen(10)
print('Waiting connection')
con, cliente = serv_socket.accept()
print('connected' )

sendPort = 7001
otherAddress = ('127.0.0.2', sendPort)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(otherAddress)

myName = input("Your name: ")
clientSocket.send(myName.encode('utf-8'))

print("Waiting for someone else to enter name ...")
clientName = con.recv(1024).decode("utf-8")
loopMessage = True
while loopMessage:

    print( "Waiting message..." )
    receive = con.recv(1024)
    
    time = datetime.now().strftime('%H:%M:%S')
    print( clientName + " at " + time + ": " + receive.decode("utf-8") )

    if receive.decode("utf-8") == "bye" or receive.decode("utf-8") == "Bye":
        print("your connection is closed because " + clientName + " sent 'Bye'")
        serv_socket.close()
        clientSocket.close()
        loopMessage = False

    else:
        message = input("I: ")
        clientSocket.send(message.encode('utf-8'))

        if(message == "Bye" or message == "bye"):
            print("your connection is closed.")
            serv_socket.close()
            clientSocket.close()
            loopMessage = False