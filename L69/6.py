class Car:
	def __init__(self):
		self.__engineno='EK1'
		self.__modelno='VX6'
	def setcarinfo(self,engineno,modelno):
		self.engineno=engineno
		self.modelno=modelno
		self.color=''
		self.year=''
	def getcarinfo(self):
		print(self.engineno,self.modelno,self.color,self.year)
honda=Car()
engno=input('engine number: ')
honda.setcarinfo(engno,'SX6')
honda.color='Blue'
honda.year='2018'
honda.getcarinfo()