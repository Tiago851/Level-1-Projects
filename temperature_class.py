#Script to create the class for converting different temperature units

#For the main unit converter scrip see: Unit Converter

class Temperatura:

	def __init__(self,tempe):
		self.tempe = tempe

	def Celcius(self):
		c = float(self.tempe)
		f = round(32+(c*(9/5)),2)
		k = round(c+273.15,2)
		
		return f"Temperature in Celcius: {c} | Fahrenheit: {f} | Kelvin: {k}"
		
	def Fahr(self):
		f = float(self.tempe)
		c = round((5/9)*(f-32),2)
		k = round((5/9)*(f+459.67),2)
		return f"Temperature in Celcius: {c} | Fahrenheit: {f} | Kelvin: {k}"

	def Kelvin(self):
		k = float(self.tempe)

		#Temperatures cannot go below absolute zero
		if  k < 0:
			return "Temperatures in Kelvin cannot be less than 0!"

		f = round((9/5)*k-459.67,2)
		c = round(k-273.15,2)
		return f"Temperature in Celcius: {c} | Fahrenheit: {f} | Kelvin: {k}"
