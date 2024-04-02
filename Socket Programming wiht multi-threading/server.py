import socket
import threading

print_lock = threading.Lock()

def createThread(c, addr):
    print(f"New connection from: {addr}")
    print(f"Thread name: {threading.currentThread().getName()}")

    while True:
        data = c.recv(1024)
        print(f"Receiving from client side: {data.decode('ascii')}")
        if not data:
            print('Bye')
            print_lock.release()
            break

        server_message = input("Enter your message: ")
        c.send(server_message.encode('utf-8'))

    c.close()

def main():
    host = "localhost"
    port = 2022

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Socket binded to port", port)
    s.listen()
    print("Server is listening")

    while True:
        c, addr = s.accept()
        print_lock.acquire()
        print(f"Connected to {addr[0]}, {addr[1]}")
        print("Thread name before creating:", threading.currentThread().getName())
        thread = threading.Thread(target=createThread, args=(c, addr))
        thread.start()

    s.close()

if __name__ == "__main__":
    main()
