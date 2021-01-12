#My code for the first calculator developed by myself.
#Props to Code.com on Youtube for helping me understand better Tkinter

#~~~~~~~~~~Modules~~~~~~~~~~
from tkinter import *
from PIL import Image,ImageTk

#~~~~~~~~~~Creating Widget~~~~~~~~~~
root=Tk()
root.title("Calculator")
root.iconbitmap("calculadora.ico")

#~~~~~~~~~~Entry field for the widget~~~~~~~~~~
e = Entry(root,width=60,borderwidth=5)
e.grid(row=0,column=0,columnspan=4)

#~~~~~~~~~~Images~~~~~~~~~~
sqrtr = Image.open("sqrtr.png")
sqrt = Image.open("square.png")
onex = Image.open("inverso.png")
sqrtr = sqrtr.resize((90,60),Image.NEAREST)
sqrt = sqrt.resize((90,60),Image.NEAREST)
onex = onex.resize((90,60),Image.NEAREST)
finalsqrt = ImageTk.PhotoImage(sqrt)
finalsqrtr = ImageTk.PhotoImage(sqrtr)
finalonex = ImageTk.PhotoImage(onex)

#~~~~~~~~~~Math Function~~~~~~~~~~
def button_click(number):
	exp = e.get()
	e.delete(0,END)
	e.insert(0,str(exp)+str(number))

def clear():
	e.delete(0,END)

def decimal():
	exp = e.get()
	e.delete(0,END)
	e.insert(0,str(exp)+".")

def adding():
	first_number = e.get()
	global f_num
	global math
	math = "Addition"
	f_num = float(first_number)
	e.delete(0,END)

def subtract():
	first_number = e.get()
	global f_num
	global math
	math = "Subtraction"
	f_num = float(first_number)
	e.delete(0,END)

def multiply():
	first_number = e.get()
	global f_num
	global math
	first_number = e.get()
	math = "Multiplication"
	f_num = float(first_number)
	e.delete(0,END)

def divide():
	first_number = e.get()
	global f_num
	global math
	math = "Division"
	f_num = float(first_number)
	e.delete(0,END)

def inverse():
	first_number = e.get()
	global f_num
	global math
	math = "Reverse"
	f_num = float(first_number)
	e.delete(0,END)

def square():
	first_number = e.get()
	global f_num
	global math
	math = "Square"
	f_num = float(first_number)
	e.delete(0,END)

def square_root():
	first_number = e.get()
	global f_num
	global math
	math = "Square Root"
	f_num = float(first_number)
	e.delete(0,END)

#~~~~~~~~~~Output~~~~~~~~~~
def equal_to():
	second_numb = e.get()
	e.delete(0,END)

	if math == "Addition":
		e.insert(0,f_num + float(second_numb))

	if math == "Subtraction":
		e.insert(0,f_num - float(second_numb))

	if math == "Division":
		e.insert(0,f_num / float(second_numb))

	if math == "Multiplication":
		e.insert(0,f_num * float(second_numb))

	if math == "Reverse":
		e.insert(0,1/f_num)

	if math == "Square":
		e.insert(0,f_num**2)

	if math == "Square Root":
		e.insert(0,f_num**0.5)

#~~~~~~~~~~Buttons~~~~~~~~~~
#Numbers
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))

#Operations
button_plus = Button(root,text="+",padx=40,pady=20,command=adding)
button_minus = Button(root,text="-",padx=40,pady=20,command=subtract)
button_times = Button(root,text="*",padx=40,pady=20,command=multiply)
button_divide = Button(root,text="/",padx=40,pady=20,command=divide)
button_reverse = Button(root,image=finalonex,padx=35,pady=20,command=inverse)
button_square = Button(root,image=finalsqrt,padx=33,pady=20,command=square)
button_square_root = Button(root,image=finalsqrtr,padx=25,pady=20,command=square_root) #text="Sqrt(x)"

#Result / Clear Input 
button_clear = Button(root,text="Clear",padx=30,pady=20,command=clear)
button_result = Button(root,text="=",padx=40,pady=20,command=equal_to)
button_comma = Button(root,text=",",padx=40,pady=20,command=decimal)

#Button Configuration
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=5,column=0)

button_plus.grid(row=4,column=3)
button_minus.grid(row=3,column=3)
button_divide.grid(row=1,column=3)
button_clear.grid(row=5,column=2)
button_result.grid(row=5,column=3)
button_times.grid(row=2,column=3)
button_comma.grid(row=5,column=1)
button_reverse.grid(row=1,column=0)
button_square.grid(row=1,column=1)
button_square_root.grid(row=1,column=2)

#~~~~~~~~~~Run Loop~~~~~~~~~~
root.mainloop()