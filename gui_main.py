# import for gui
import tkinter as tk
from tkinter import filedialog, messagebox

# importing the organize function
from core.organizer import organize_folder
# importing the loading settings function from utils
from core.utils import load_settings


# loading the settings and getting file types from it
settings = load_settings("config/settings.yaml")
# storing the file types
file_types = settings["file_types"]

# help user navigate the file directory and hold the selected directory
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)

# initiate the organizing process
def start_organizing():
    folder_path = entry.get().strip()
    if folder_path:
        organize_folder(folder_path, file_types)
        messagebox.showinfo("Done", "Files have been organized successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a folder.")

# Create window
root = tk.Tk()
root.title("Smart File Organizer")
root.geometry("400x200")

# Folder entry
label = tk.Label(root, text="Select Folder to Organize:")
label.pack(pady=10)

# where user select directory
entry = tk.Entry(root, width=40)
# make enter stick to the window
entry.pack()

# create a button that will tigger directory selection
browse_btn = tk.Button(root, text="📁 Browse", command=browse_folder)
# add some pixel to it
browse_btn.pack(pady=5)

# start the organization process
start_btn = tk.Button(root, text="🚀 Start Organizing", command=start_organizing)
# add some padding
start_btn.pack(pady=15)

# allow the window to be open till user close it
root.mainloop()