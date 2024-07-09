import tkinter as tk
from tkinter import ttk
import os
import shutil

# Home Screen
def home_screen():
    root = tk.Tk()
    root.title("PyWorld")

    # Home Screen Elements
    home_label = tk.Label(root, text="Welcome to PyWorld!")
    send_button = tk.Button(root, text="Send Your Projects", command=send_projects)
    download_button = tk.Button(root, text="Download Projects", command=download_projects)

    # Layout
    home_label.pack(pady=20)
    send_button.pack(pady=10)
    download_button.pack(pady=10)

    root.mainloop()

# Send Projects
def send_projects():
    send_window = tk.Toplevel()
    send_window.title("Send Your Projects")

    # Send Projects Elements
    file_label = tk.Label(send_window, text="Select a Python file:")
    file_entry = tk.Entry(send_window)
    send_button = tk.Button(send_window, text="Send", command=lambda: upload_file(file_entry.get()))

    # Layout
    file_label.pack(pady=10)
    file_entry.pack(pady=10)
    send_button.pack(pady=10)

# Upload File
def upload_file(file_path):
    if os.path.isfile(file_path) and file_path.endswith(".py"):
        # Copy the file to the projects directory
        projects_dir = "projects"
        if not os.path.exists(projects_dir):
            os.makedirs(projects_dir)
        shutil.copy(file_path, os.path.join(projects_dir, os.path.basename(file_path)))
        print(f"File '{os.path.basename(file_path)}' uploaded successfully!")
    else:
        print("Invalid file. Please select a valid Python file.")

# Download Projects
def download_projects():
    download_window = tk.Toplevel()
    download_window.title("Download Projects")

    # Download Projects Elements
    projects_dir = "projects"
    if not os.path.exists(projects_dir):
        os.makedirs(projects_dir)

    project_listbox = tk.Listbox(download_window, width=50)
    project_listbox.pack(pady=10)

    for filename in os.listdir(projects_dir):
        if filename.endswith(".py"):
            project_listbox.insert(tk.END, filename)

    download_button = tk.Button(download_window, text="Download", command=lambda: download_file(project_listbox.get(project_listbox.curselection())))
    download_button.pack(pady=10)

# Download File
def download_file(filename):
    projects_dir = "projects"
    file_path = os.path.join(projects_dir, filename)
    if os.path.isfile(file_path):
        # Open the file in the default application
        os.startfile(file_path)
    else:
        print(f"File '{filename}' not found.")

# Run the Home Screen
home_screen()
