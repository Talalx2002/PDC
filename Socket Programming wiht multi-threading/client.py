import socket

host = '127.0.0.1'
port = 2022

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    message = input("Enter your message: ") 
    s.send(message.encode('utf-8'))
    
    if message.lower() == 'bye':  
        print("Bye Server")
        break

    data = s.recv(1024)
    print('Received from the server:', str(data.decode('utf-8')))
    
s.close() 
