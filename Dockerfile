FROM python:3.8.10

COPY . /scripts
WORKDIR /scripts/

RUN apt-get update && apt-get -y install sudo
RUN pip3 install -y tqdm
RUN pip3 install -y requests
RUN pip3 install -y cryptography

# Runing the scripts
RUN python3 server_file.py
RUN python3 client_file.py
RUN python3 decrypt_file.py

