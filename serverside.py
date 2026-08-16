import socket
import ngrok

ngrokToken = "3HyzaTZHwEjTDYAwU0XYRX6Jshc_44xz1euDXComEJHTU9B1N"

listener = ngrok.forward("localhost:8080", authtoken=ngrokToken, proto="tcp")

print(f"Listener established at: {listener.url()}");


# Create an IPv4 TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen()

while True:
    # Accept connection from client program
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    try:
        # Receive data up to 4096 bytes and decode it
        data = conn.recv(4096).decode('utf-8')
        if data:
            print(f"{data}")
            
    finally:
        conn.close()