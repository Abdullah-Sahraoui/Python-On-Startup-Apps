import tkinter as tk
import os
from tkinter import filedialog
from functools import partial

root = tk.Tk()
apps = []

root.title("On StartUp App")

def read_from_file():
  if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
      files = f.read()
      temp_apps = files.split(",")
      global apps 
      apps = temp_apps
    

    

def save_to_file():
  with open("save.txt", "w") as f:
    # Deleting file's contents to avoid copying same links:
    f.truncate()

    # Joining each app in apps with a comma:
    f.write(",".join(apps))
    f.close()

def remove_app(app):
  apps.remove(app)
  print_files()
  save_to_file()


def print_files():
  for widget in frame.winfo_children():
    widget.destroy()
  for app in apps:
    label = tk.Label(frame, text=app)
    label.grid(row=apps.index(app), column=0)

    remove_with_arg = partial(remove_app, app)
    delete = tk.Button(frame, text="Delete", fg="white", bg="crimson", command=remove_with_arg)
    delete.grid(row=apps.index(app), column=1)


def open_file():

  filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
  apps.append(filename)
  print_files()
  save_to_file()


def run_apps():
  for app in apps:
    os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="skyblue")
canvas.pack(fill="both", expand=True)

frame = tk.Frame(root, bg="white")
frame.pack(fill="both", expand=True)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button_one = tk.Button(root, text="Open File", bg="navy", fg="white", command=open_file)
button_one.pack()

buttonTwo = tk.Button(root, text="Run Apps", bg="navy", fg="white", command=run_apps)
buttonTwo.pack()


read_from_file()
print_files()

root.mainloop()