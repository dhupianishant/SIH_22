from tkinter import *
from  tkinter import  ttk

def regsiter(): 
	mon1=monument.get()
	mob1=mobile.get()
	date1=date.get()
	age1=age.get()
	gender1=gender.get()
	mail1=mail.get()
	

def registrationform():
	global reg_screen
	reg_screen = Tk()
	reg_screen.title("eTicketing System for Monuments")
	reg_screen.geometry("350x400")
	global message
	global monument
	global mobile
	global date
	global age
	global gender
	global mail
	global name
	monument = StringVar()
	mobile = StringVar()
	date = StringVar()
	age = StringVar()
	gender = IntVar()
	mail = StringVar()
	name = StringVar()

	#Layout
	Label(reg_screen, width="300", text="Please Enter you details below.").pack()
	
	#Monuments
	Label(reg_screen, text="Select Monument: ").place(x=20, y=20)
	monchosen=ttk.Combobox(reg_screen, width=27, textvariable=monument)
	monchosen['values'] = ("Taj Mahal, Agra", "Hawa Mahal, Jaipur", "Statue of Unity, Gujarat")
	monchosen.current()
	monchosen.place(x=20, y=40)

        #Name
	Label(reg_screen, text="Name:  ").place(x=20, y=80)
	Entry(reg_screen, textvariable=name).place(x=90, y=82)

	#Mobile
	Label(reg_screen, text="Mobile No.: ").place(x=20, y=120)
	Entry(reg_screen, textvariable=mobile).place(x=90, y=122)
	
	#Date
	Label(reg_screen, text="Date: ").place(x=20,y=160)
	Entry(reg_screen, textvariable=date).place(x=90,y=162)

	#Age
	Label(reg_screen, text="Age: ").place(x=20,y=200)
	Entry(reg_screen, textvariable=age).place(x=90,y=202)

	#Gender
	Label(reg_screen, text="Gender: ").place(x=20,y=240)
	Radiobutton(reg_screen, text="Male", variable=gender, value=1).place(x=90, y=242)
	Radiobutton(reg_screen, text="Female", variable=gender, value=2).place(x=150, y=242)

	#Mail
	Label(reg_screen, text="Mail ID: ").place(x=20,y=280)
	Entry(reg_screen, textvariable=mail).place(x=90,y=282)	

        #button
	Button(reg_screen, text="Register", width=10, height=1, bg="orange", command=regsiter).place(x=105, y=320)
	reg_screen.mainloop()
registrationform()
