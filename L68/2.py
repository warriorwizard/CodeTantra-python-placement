class Car:
	def setbrandname(self, brandname):
		self.brandname=brandname
		
	def getbrandname(self):
		print(self.brandname)
		
	def setmodel(self, model):
		self.model=model
		
	def getmodel(self):
		# Write your code here
		print(self.model)
		
class Accord(Car):
	def setbrandname(self, brandname):
		self.brandname=brandname
	def getbrandname(self):
		print(self.brandname)
blueaccord = Accord()
# set the brand and model name by taking the input from the user 
brand=input('brand: ')
model=input('model: ')
blueaccord.setbrandname(brand)
blueaccord.setmodel(model)
blueaccord.getbrandname()
blueaccord.getmodel()
