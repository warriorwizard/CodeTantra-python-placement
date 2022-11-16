class Car:
	def setenginemodel(self, engine):
		self.engine = engine
	def getenginemodel(self):
		print(self.engine)
class Tyre:
	def settyrenumber(self, num):
		self.num = num
	def gettyrenumber(self):
		print(self.num)
class Honda(Car, Tyre):
	def setcarmodel(self, model):
		self.model = model
	def getcarmodel(self):
		print(self.model)
accord = Honda()
accord.setenginemodel('EK-1')
accord.setcarmodel('V6')
accord.settyrenumber(236)
print('Car Details: ')
accord.getenginemodel()
accord.getcarmodel()
accord.gettyrenumber()