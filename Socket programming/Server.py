import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1027))
s.listen(5)
print("Server is listening...") 
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Socket programming in python ", "utf-8"))
    clientsocket.close()