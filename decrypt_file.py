from cryptography.fernet import Fernet
import os

BUFFER_SIZE = 4096

def load_key():
    #Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()

# load the previously generated key
key = load_key()
# initialize the Fernet class
aes = Fernet(key)

# the name of file we want to send, make sure it exists
t=int(input("Enter 1 for app, 2 for sysad and 3 for web file : "))
if(t==1):
    fname="app.txt"
elif(t==3):
    fname="web.txt"
elif(t==2):
    fname="sysad.txt"
else:
    fname="error.log"

# remove absolute path if there is
filename = os.path.basename(fname)

file = open(fname, "w")  

with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break

        # encrypt the message
        bytes_read = aes.decrypt(bytes_read)

        file.write(bytes_read.decode()) 

file.close()