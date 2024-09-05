import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil

# Home Screen
def home_screen():
    root = tk.Tk()
    root.title("PyCloud")

    # Menu Bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    
    # Add Rules Menu
    rules_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Rules", menu=rules_menu)
    rules_menu.add_command(label="View Rules", command=view_rules)

    # Home Screen Elements
    home_label = tk.Label(root, text="Welcome to PyCloud!")
    send_button = tk.Button(root, text="Add files", command=send_projects)
    download_button = tk.Button(root, text="Get files", command=download_projects)

    # Layout
    home_label.pack(pady=20)
    send_button.pack(pady=20)
    download_button.pack(pady=20)

    root.mainloop()

# Send Projects
def send_projects():
    send_window = tk.Toplevel()
    send_window.title("Add files")

    # Send Projects Elements
    file_label = tk.Label(send_window, text="Select a Python file:")
    file_entry = tk.Entry(send_window)
    browse_button = tk.Button(send_window, text="Browse", command=lambda: browse_file(file_entry))
    
    desc_label = tk.Label(send_window, text="File Description (Optional but needed because there s a problem. Wait till we fix it.):")
    desc_text = tk.Text(send_window, height=5, width=40)
    
    send_button = tk.Button(send_window, text="Send", command=lambda: upload_file(file_entry.get(), desc_text.get("1.0", tk.END).strip()))

    # Layout
    file_label.pack(pady=10)
    file_entry.pack(pady=10)
    browse_button.pack(pady=5)
    desc_label.pack(pady=10)
    desc_text.pack(pady=10)
    send_button.pack(pady=10)

# Browse File
def browse_file(file_entry):
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Upload File
def upload_file(file_path, description):
    if os.path.isfile(file_path) and file_path.endswith(".py"):
        projects_dir = "projects"
        descriptions_dir = "descriptions"
        
        if not os.path.exists(projects_dir):
            os.makedirs(projects_dir)
        if not os.path.exists(descriptions_dir):
            os.makedirs(descriptions_dir)

        shutil.copy(file_path, os.path.join(projects_dir, os.path.basename(file_path)))
        
        desc_filename = os.path.splitext(os.path.basename(file_path))[0] + ".txt"
        with open(os.path.join(descriptions_dir, desc_filename), "w") as desc_file:
            desc_file.write(description)
        
        messagebox.showinfo("Success", f"File '{os.path.basename(file_path)}' uploaded successfully with description!")
    else:
        messagebox.showerror("Error", "Invalid file. Please select a valid Python file.")

# Download Projects
def download_projects():
    download_window = tk.Toplevel()
    download_window.title("Download Projects")

    projects_dir = "projects"
    if not os.path.exists(projects_dir):
        os.makedirs(projects_dir)

    project_listbox = tk.Listbox(download_window, width=50)
    project_listbox.pack(pady=10)

    for filename in os.listdir(projects_dir):
        if filename.endswith(".py"):
            project_listbox.insert(tk.END, filename)

    download_button = tk.Button(download_window, text="retrive files", command=lambda: download_file(project_listbox))
    view_desc_button = tk.Button(download_window, text="View Description", command=lambda: view_description(project_listbox))
    download_button.pack(pady=10)
    view_desc_button.pack(pady=10)

# Download File
def download_file(project_listbox):
    try:
        selected_file = project_listbox.get(project_listbox.curselection())
        projects_dir = "projects"
        file_path = os.path.join(projects_dir, selected_file)
        if os.path.isfile(file_path):
            os.startfile(file_path)
        else:
            messagebox.showerror("Error", f"File '{selected_file}' not found.")
    except tk.TclError:
        messagebox.showerror("Error", "No file selected. Please select a file to get.")

# View Description
def view_description(project_listbox):
    try:
        selected_file = project_listbox.get(project_listbox.curselection())
        descriptions_dir = "descriptions"
        desc_filename = os.path.splitext(selected_file)[0] + ".txt"
        desc_path = os.path.join(descriptions_dir, desc_filename)
        
        if os.path.isfile(desc_path):
            with open(desc_path, "r") as desc_file:
                description = desc_file.read()
            messagebox.showinfo("Project Description", description)
        else:
            messagebox.showerror("Error", f"Description for '{selected_file}' not found.")
    except tk.TclError:
        messagebox.showerror("Error", "No project selected. Please select a file to view its description.")

# View Rules
def view_rules():
    rules_window = tk.Toplevel()
    rules_window.title("Community Rules")

    rules_text = """
    Welcome to PyCloud community!

    rules:
    1. No illegal files here: Do we even look like we are going to put illegal nuke codes here? AND WE SAY HERE NO TO THE GOVERMENT BECAUSE THEY MAY STORE MORE ILLEGAL STUFF THAN  CRIMINALS DO >:(
    2. No NSFW pictures or videos or other stuff: Okay do we look like we are nnot watching you? We have a software called ContentChecker which sees all content in yur files to see if they are with us or aganst us.
    3. No what is illegal: We don't allow anything illegal here >:) *Doom music plays*

    Let's make PyCloud the best as ever!
    """

    rules_label = tk.Label(rules_window, text=rules_text, justify=tk.LEFT, padx=10, pady=10)
    rules_label.pack()

# Run the Home Screen
home_screen()
