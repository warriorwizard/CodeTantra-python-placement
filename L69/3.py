class Student:
	name=""
	age=''
	__group='ECE'
	__report='Fail'
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def setDetails(self,__group,__report):
		self.__group=__group
		self.__report=__report
	def getdetails(self):
		print(self.name,self.age,self.__group,self.__report)
# write your code here





print("Student Report Card")
s1 = Student('SriRam', '19')
s1.setDetails("CSC", "pass")
s1.getdetails()