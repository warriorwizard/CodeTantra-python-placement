class Car:
	def setName(self,name):
		self.name=name
	def getName(self):
		return self.name
	
Honda=Car()
a=input('car name: ')
Honda.setName(a)
print('Honda car name:',Honda.getName())