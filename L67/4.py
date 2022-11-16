class Person:
	def setname(self,name):
		self.name=name
	def getname(self):
		print(self.name)
class Student(Person):
	def setage(self,age):
		self.age=age
	def getage(self):
		print(self.age)
		
name=input('Please enter a name: ')
age=int(input('Please enter age: '))

s1=Student()
s1.setname(name)
s1.setage(age)
s1.getname()
s1.getage()