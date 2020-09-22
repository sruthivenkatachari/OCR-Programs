from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import os.path
import time



HEIGHT=500
WIDTH=600
window=tk.Tk()
window.title('Currency Analyser')
window.iconbitmap('C:/New folder (3)/icon.ico')
window.geometry ("700x600+400+100")


f1=Frame(window)
f2=Frame(window)

def swap(frame):
	frame.tkraise()

def create():	
	new =Toplevel(window)


def mquit():
	mess=messagebox.askyesno(title="quit",message="Are you sure to quit")	


def mfileopen():
    file1=filedialog.askopenfile()
    label=Label(text=file1).grid()
    file2=file1.name
    f=open(file2,encoding="cp437")
    label2=Label(text=f.read()).grid()	


for frame in (f1,f2):
	frame.grid(row=0,column=0)

canvas=tk.Canvas(window,height=HEIGHT,width=WIDTH)
canvas.grid()

my_img=ImageTk.PhotoImage(Image.open("note.jpg"))
my_label=Label(image=my_img)
my_label.grid(row=0,column=0,columnspan=2)



button_next=Button(window,text="Continue",command=lambda: swap(f2))
button_quit=Button(window,text="close",command=window.quit)
button_quit.grid(row=1,column=0)
button_next.grid(row=1,column=1)


#my_label1=Label(window,text="Welcome to search optimization",padx=200,pady=200,bg='light blue',fg="white",font=("Times New Roman",14)).grid()
button_choose=Button(frame,text="choose the file",height="2",width="20",command=mfileopen).grid()

button_close=Button(frame,text="close",height="2",width="20",command=window.quit).grid()

mymenu=Menu()
listone=Menu()
listone.add_command(label="New File")
listone.add_command(label="Open File")
listone.add_command(label="Save File")
listone.add_command(label="Quit",command=mquit)

listtwo=Menu()
listtwo.add_command(label="undo")
listtwo.add_command(label="redo")
  
mymenu.add_cascade(label="File",menu=listone)
mymenu.add_cascade(label="Edit",menu=listtwo)
mymenu.add_cascade(label="Tools")
mymenu.add_cascade(label="Help")

window.config(menu=mymenu)

f1.tkraise()

window.mainloop() 