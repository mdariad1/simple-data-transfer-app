## How to Use

1. Run the `server.py` script. This will start the server on `localhost` port `12345`.
2. Run the `client.py` script. This will open a GUI window.
3. In the GUI, you can choose to upload or download files. To upload a file, click on the 'Upload' button and select a file from your system. To download a file, select a file from the list of available files and click on the 'Download' button.

## Functionality

The `server.py` script sets up a server that listens for incoming connections. When a client connects, it waits for a command from the client. The command can be either 'upload' or 'download', followed by a filename. If the command is 'upload', the server receives a file from the client and saves it in the 'database' directory. If the command is 'download', the server sends a file from the 'database' directory to the client.

The `client.py` script provides a GUI for the user to interact with the server. It displays a list of files currently available in the 'database' directory on the server. The user can select a file to download or choose a file from their system to upload. The script handles the file transfer using the 'send_file' and 'receive_file' functions.
