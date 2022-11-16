class Car:
	def setDetails(self, model, regno):
		self.model=model
		self.regno=regno
	def getModel(self):
		return self.model
		
	def getRegno(self):
		# write your code here
		return self.regno
Hyundai = Car()
Maruthi = Car()
#Take details of the car as input from user. Write your code here
a=input('car1 model: ')
b=input('car1 regno: ')
c=input('car2 model: ')
d=input('car2 regno: ')
Hyundai.setDetails(a,b)
Maruthi.setDetails(c,d)

print("Hyundai car details:",Hyundai.getModel() , Hyundai.getRegno())
print("Maruthi car details:",Maruthi.getModel(), Maruthi.getRegno())