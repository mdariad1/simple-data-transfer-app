import glob
import socket
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def show_success_popup(message):
    messagebox.showinfo("Success", message)

def show_error_popup(message):
    messagebox.showerror("Error", message)
def send_file(sock, filename):
    with open(filename, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            sock.sendall(data)

def receive_file(sock, filename):
    with open(filename, 'wb') as file:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file.write(data)


def start_client():
    window = tk.Tk()
    window.geometry("600x300")  # Width x Height

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)
    button_frame.place(relx=0.25, rely=0.6, anchor='center')

    # Create a frame to hold the listbox
    listbox_frame = tk.Frame(window)
    listbox_frame.place(relx=0.75, rely=0.5, anchor='center')

    # Create a label for the listbox
    listbox_label = tk.Label(listbox_frame, text="Available files", font=("Arial", 20))
    listbox_label.pack(pady=10)

    # Create a listbox to display the file names
    listbox = tk.Listbox(listbox_frame, width=40, height=10)
    listbox.pack(pady=10)


    def update_listbox():
        # Clear the listbox
        listbox.delete(0, tk.END)
        # Add the current files in the 'database' directory to the listbox
        for filename in glob.glob('database/*'):
            listbox.insert(tk.END, filename.replace('database/', ''))

    def upload_file():
        filename = filedialog.askopenfilename()
        if filename:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(('localhost', 12345))
                sock.sendall(f'upload {os.path.basename(filename)}'.encode())
                send_file(sock, filename)
                sock.close()
                update_listbox()  # Update the listbox after the operation
                show_success_popup(f"File {filename} uploaded successfully")
            except Exception as e:
                show_error_popup(f"Error uploading file: {str(e)}")

    def download_file():
        filename = filedialog.askopenfilename(initialdir='database')
        if filename:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(('localhost', 12345))
                sock.sendall(f'download {os.path.basename(filename)}'.encode())
                # Check if 'downloaded' directory exists, if not, create it
                if not os.path.exists('downloaded'):
                    os.makedirs('downloaded')
                # Save the downloaded file in the 'downloaded' directory
                receive_file(sock, f'downloaded/{os.path.basename(filename)}')
                sock.close()
                update_listbox()  # Update the listbox after the operation
                show_success_popup(f"File {filename} downloaded successfully")
            except Exception as e:
                show_error_popup(f"Error uploading file: {str(e)}")

    upload_button = tk.Button(button_frame, text="Upload a file", command=upload_file, height=3, width=20, bg='lightblue', fg='black')
    upload_button.pack(pady=10)  # Add some vertical padding

    download_button = tk.Button(button_frame, text="Download a file", command=download_file, height=3, width=20, bg='lightblue', fg='black')
    download_button.pack(pady=10)  # Add some vertical padding

    update_listbox()  # Update the listbox when the client starts

    window.mainloop()


if __name__ == "__main__":
    start_client()
