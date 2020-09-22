from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter import filedialog



	# basic window config

window=Tk()  # gui window
window.title("Currency Analyser") #window title
window.iconbitmap('C:/New folder (3)/icon.ico')
fgcolour="#ffffff"  # font colour
bgcolour="#000000"  # background colour
text=("verdana",12)
window.configure(bg="#840DE8") # background colour
window.geometry("600x400")  #window size

# background image for app
bgImage=PhotoImage(file=r"C:/New folder (3)/IndianCurrency.png")
Label(window,image=bgImage).place(relwidth=1,relheight=1)


def mquit():
	mess=messagebox.askyesno(title="quit",message="Are you sure to quit")
	# main title and frame for the program

titleFrame= Frame(window,bg=bgcolour)
titleFrame.place(relwidth=1,relheight=0.08)

	# main title label widget
Label(titleFrame, 
		text='Welcome',
		font=text,
		anchor= CENTER,
		fg=fgcolour,
		bg=bgcolour).place(relx=0,relheight=1)


	

	# instruction label widget
instruction=Label(window,
	 	fg=fgcolour,
	 	bg=bgcolour,
	 	text="Instructions:",
	 	anchor= CENTER,
	 	font= text
	 	)

	
instruction.place(relx=0.1,
	 	rely=0.15,
	 	relwidth=0.8,
	 	relheight=0.1)	


	# instructions  steps Label widgets

steps=Label(window,
		fg=fgcolour,
		bg="#303030",
		font=text,text="You have created a frame")

steps.place(relx=0.1,
		rely=0.25,
		relwidth=0.8,
		relheight=0.6)

	# assigning image fro the button

exitImg=PhotoImage(file=r"C:/New folder (3)/button.png")

	

	# Exit Button
exit=Button(window,
		text="Exit",image=exitImg,
		compound=CENTER,
		command=window.quit)

exit.place(relx=0.2,
	rely=0.9,
	relwidth=0.15,
	relheight=0.08)		

	# next button

nextbutton= Button(window,
		image=exitImg,
		text="Next",
		compound=CENTER)

nextbutton.place(relx=0.65,
		rely=0.9,
		relwidth=0.15,
		relheight=0.08)
	





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




window.mainloop()

# call procedure