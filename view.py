from logging import root
from tkinter import *
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from api import process

def importimage(): 
    fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(("JPG file", "*.jpg"), ("PNJ file", "*.png"), ("All Files", "*.*")))
    img = Image.open(fln)
    img.thumbnail((350,350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

# def importvideo():
    # fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(("JPG file", "*.jpg"), ("PNJ file", "*.png"), ("All Files", "*.*")))

root = Tk()

frame = Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)
lbl=Label(root )
lbl.pack()

btn = Button(frame, text="Browse Image", command= importimage)
btn.pack(side=tk.LEFT)

# btn2 = Button(frame, text="Browse Vidéo", command=lambda: exit())
# btn2.pack(side=tk.LEFT, padx=10)

btn2 = Button(frame, text="Proceed", command=lambda: process("./Cameron.jpg","./00.01.20.760-00.01.21.918.mp4"))
btn2.pack(side=tk.LEFT)

# btn3 = Button(frame, text="Brwose video", command= importvideo)
# btn3.pack(side=tk.LEFT)

root.title("image browser")
root.geometry("300x350")
root.mainloop()