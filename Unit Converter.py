#This is my very first unit converted developed based on my knowledge about Tkinter and Python
#The main objective here is to learn and experiment with Tkinter

#The scripts for temperature and mass conversion are also uploaded in this repository

#Main Modules and packages
from tkinter import *
from tkinter import messagebox
from temperature_class import Temperatura as tempclass
from mass_class import Massa as mass_class

#Widget to choose what the user wants to convert
root = Tk()
root.title("Choose Conversion")
root.geometry("300x120")

r = IntVar()

choices_unit = [("Temperature",1),("Mass",2)]

#Choose the type of conversion you need
Label(root,text="Choose what kind of conversion you'd like to make:").pack(anchor=NW)

for a,b in choices_unit:
	Radiobutton(root,text=a,variable=r,value=b).pack(anchor=W)
	
def opchoice(value):
	Label(root,text=value).pack()
	global userchoice

	if r.get() == 1:
		userchoice = 1
		root.quit()

	elif r.get() == 2:
		userchoice = 2
		root.quit()

def quit_choice():
	global userchoice
	userchoice = 0
	root.quit()

Button(root,text="Continue",command=lambda:opchoice(r.get())).pack()
Button(root,text="Quit Converter",command=quit_choice).pack() #quit_choice).pack()

root.mainloop()

#As soon as the user chooses the type of conversion, I wanted the first widget to disappear
root.destroy()

#I specifically wanted a second, independent widget to pop up and not Toplevel-kind of widgets
#Even though I read on StackOverflow that this is not 100% advisable I wanted to experiment :)
root2 = Tk()
e = Entry(root2,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)
root2.geometry("400x50")

#The output from the choice above will determine which type of conversion will take place 
if userchoice == 1:

	root2.title("Temperature Conversion")
	
	temp = StringVar(root2)
	temp_units = {1:"Celcius",2:"Fahrenheit",3:"Kelvin"}
	temp.set("Celcius")

	drop = OptionMenu(root2,temp,*temp_units.values())
	drop.grid(row=0,column=3,columnspan=1)
	
	def showt(*args):
		for i,j in temp_units.items():
			unit = tempclass(e.get())
			if temp.get() == "Celcius":
				y = unit.Celcius()
				Label(root2,text=y).grid(row=1,column=0,columnspan=5)

			elif temp.get() == "Fahrenheit":
				y = unit.Fahr()
				Label(root2,text=y).grid(row=1,column=0,columnspan=5)

			else:
				y = unit.Kelvin()
				Label(root2,text=y).grid(row=1,column=0,columnspan=5)
	
	Button(root2,text="Convert",command=showt).grid(row=0,column=4)

	root2.mainloop()
	
elif userchoice == 2:

	root2.title("Mass Conversion")

	mass = StringVar(root2)
	mass_units = {1:"Kilograms",2:"Ounces",3:"Pounds"}
	mass.set("Kilograms")

	drop = OptionMenu(root2,mass,*mass_units.values())
	drop.grid(row=0,column=3,columnspan=1)

	def showm(*args):

		if float(e.get()) < 0:
			messagebox.showwarning("Nope","Mass cannot be negative!")
			e.delete(0,END)
			fi = "Please introduce the temperature again."	

		elif mass.get() == "Kilograms":
			fi = mass_class(e.get()).kilos()

		elif mass.get() == "Ounces":
			fi = mass_class(e.get()).ounces()

		else:
			fi = mass_class(e.get()).pounds()

		messagebox.showinfo("Results",fi)

	Button(root2,text="Convert",command=showm).grid(row=0,column=4)

	root2.mainloop()

else:
	root2.destroy()