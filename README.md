## AlphaQ File Server - Delta Sys Ad Task 3

AlphaQ File Server
Dipesh needs a file server to share files between members. Your task is to create a file server and client to send and receive files using sockets.

## Usage - Script

Server file: This will get the server up and running (on port 8888)

*     python3 server_file.py

Client file:

*     python3 client_file.py

Decrypt

*     python3 decrypt_file.py

## Usage - Docker

Docker

*     docker build -t alphaq-ftp .

## Normal Mode
<li>Clients must be able to receive files of respective domains(SysAd, WebDev, AppDev) from the file server. <b>Done</b>
<li>Multiple clients must be able to download files at same time. <b>Done</b>  (For small files)
<li>Dockerize the server. <b>Done</b>
  
## Superuser Mode
<li>Users must be able to upload files to the server.
<li>Users must be able to search for files in the server using regex.
<li>Enable authentication for uploading/downloading/removing files.
<li>Encrypt the files being transfered using (AES-256). <b>Done</b>
  
### Submitted by Akash Jaiswal
