#Script to create the class for converting different mass units
#For simplicity sake, only 3 units were included
#Conversion from https://www.unitconverters.net/

#For the main unit converter scrip see: Unit Converter

from tkinter import messagebox

class Massa:

	def __init__(self,massa):
		self.massa = massa

	def kilos(self):
		k = float(self.massa)
		p = k*2.2046244202
		o = k*35.273990723
		y = f"Kilos: {k} | Pounds: {p} | Ounces: {o}"
		return y

	def ounces(self):
		o = float(self.massa)
		k = o*0.0283495
		p = o*0.0625
		y = f"Kilos: {k} | Pounds: {p} | Ounces: {o}"
		return y
		
	
	def pounds(self):
		p = float(self.massa)
		k = p*0.453592
		o = p*16
		y = f"Kilos: {k} | Pounds: {p} | Ounces: {o}"
		return y