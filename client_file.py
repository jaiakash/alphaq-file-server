import socket
import tqdm
from cryptography.fernet import Fernet
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
#TODO using localhost for testing purpose
host = "localhost"
port = 8888

def write_key():
    #Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def load_key():
    #Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()

# the name of file we want to send, make sure it exists
t=int(input("Enter 1 for app, 2 for sysad and 3 for web file : "))
if(t==1):
    fname="fapp.txt"
elif(t==3):
    fname="fweb.txt"
elif(t==2):
    fname="fsysad.txt"
else:
    fname="ferror.log"


filename = "./files/"+fname;
# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# load the previously generated key
key = load_key()
# initialize the Fernet class
aes = Fernet(key)

# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break

        # encrypt the message
        bytes_read = aes.encrypt(bytes_read)

        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()