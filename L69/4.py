class Student:
	name=""
	age=""
	group=""
	report=""
	def setDetails(self,name,age,group,report):
		self.name=name
		self.age=age
		self.group=group
		self.report=report
	def getDetails(self):
		print(self.name,self.age,self.group,self.report)
s1=Student()
name=input('name: ')
age=input('age: ')
group=input('group: ')
report=input('report: ')
s1.setDetails(name,age,group,report)
s1.getDetails()
		