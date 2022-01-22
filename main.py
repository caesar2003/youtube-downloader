from tkinter import filedialog
import pytube
import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font
from tkinter import *
import os

username = os.getlogin()
root = tk.Tk()
def addPath():
    global folder_path
    global filename
    filename = filedialog.askdirectory(initialdir="/")
    folder_path.set(filename)

def download():
    url = entry.get()
    try:
        video = pytube.YouTube(url).streams.get_highest_resolution()
        try:
            video.download(filename)
        except:
            video.download(f'C:/Users/{username}/Downloads')
    except:
        print("Etwas stimmt nicht mit der URL")
        


root["bg"] = "#17141d"
w = 800 
h = 650 
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


frame = tk.Frame(root, bg='#17141d')
frame.place(relwidth=1, relheight=1)

folder_path = StringVar(value=f'C:/Users/{username}/Downloads')
filename = StringVar()
openFile = tk.Button(frame, text="OpenPath",font=("Montserrat 12"), padx="20", pady="10", fg="white", bg="#cd211f",borderwidth="0", command=addPath)
openFile.place(relx=0.5, rely=0.5, anchor=CENTER)

btnDownload = tk.Button(frame, text="Download",font=("Montserrat 12"), padx="20", pady="10", fg="white", bg="#cd211f",borderwidth="0", command=download)
btnDownload.place(relx=0.95, rely=0.95, anchor=SE)

label = tk.Label(frame, textvariable=folder_path,font=("SegoeUISemilight 12"), bg="#17141d", fg="white",)
label.place(rely=0.57, relx=0.5, anchor=CENTER)


entry = Entry(frame, font=("Montserrat 16"))
entry.insert(0,"Paste Url")
entry.place(relwidth=0.9, relx=0.5,rely=0.1, anchor=N)






root.mainloop()
