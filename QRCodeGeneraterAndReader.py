# QR Code Generator

# Importing Modules
from tkinter import *
from tkinter import messagebox
import os
import pyqrcode

# Defining Window
root = Tk()
root.title("QR Code Generator")

# Showing The User to intsall Important Modules to Make Sure the Code Works Perfectly.
messagebox.showinfo("Important!", '''Make Sure To Install pyqrcode & pypng.

in cmd type:
python -m pip install pyqrcode
python -m pip install pyqrcode

Ignore If Already Installed.''')

# Definig Functions


def generate():
    if len(Sub.get()) != 0:
        global qr, qrimg
        qr = pyqrcode.create(Sub.get())
        qrimg = BitmapImage(data=qr.xbm(scale=10))
    else:
        messagebox.showinfo("Warning!", "Enter Data!")
    try:
        showqr()
    except:
        pass


def showqr():
    ImageLabel.config(image=qrimg)
    SubLabel.config(text="QR of" + " " + Sub.get())


def save():
    dir = os.getcwd() + "\\QR Code"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(Name.get()) != 0:
            qr.png(os.path.join(dir, Name.get()+".png"), scale=10)
            messagebox.showinfo("Success!", "QR Code Saved.")
        else:
            messagebox.showinfo("Warning!", "Enter File Name!")
    except:
        messagebox.showinfo("Warning!", "Genetare QR First!")


Input = Label(root, text="Data To Make QR Of:")
Input.grid(row=0, column=0, sticky=N+S+W+E)

FileName = Label(root, text="Enter Name To Save As:")
FileName.grid(row=1, column=0, sticky=N+S+W+E)

Sub = StringVar()
SubEntry = Entry(root, textvariable=Sub)
SubEntry.grid(row=0, column=1, sticky=N+S+W+E)

Name = StringVar()
NameEntry = Entry(root, textvariable=Name)
NameEntry.grid(row=1, column=1, sticky=N+S+W+E)

GenButton = Button(root, text="Generate", width=14, command=generate)
GenButton.grid(row=0, column=3, sticky=N+S+W+E)

SaveButton = Button(root, text="Save", width=14, command=save)
SaveButton.grid(row=1, column=3, sticky=N+S+W+E)

ImageLabel = Label(root)
ImageLabel.grid(row=2, column=1, sticky=N+S+W+E)

SubLabel = Label(root, text="")
SubLabel.grid(row=3, column=1, sticky=N+S+W+E)

# Making The UI Responsive
TotRows = 3
TotColumns = 3

for i in range(TotRows+1):
    root.grid_rowconfigure(i, weight=1)

for j in range(TotColumns+1):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
