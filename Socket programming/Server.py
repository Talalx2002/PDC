import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1027))
s.listen(5)
print("Server is listening...") 

input = input("Enter a message: ")  

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes(input, "utf-8"))
    clientsocket.close()    