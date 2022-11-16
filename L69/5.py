class Student:
	def __init__(self):
		self.__name = "SriRam"
		self.__age = "19"
		self.__group = "ECE"
		self.__report = "fail"
 
	def __setdetails(self,__group,__report):
		self.__group=__group
		self.__report=__report
	def setgroup(self,group,report):
		self.group=group
		self.report=report

	def getdetails(self):
		print(self.__name,self.__age,self.group,self.report)
# define a public method getdetails here

	#print student name, age, group, report here 

s1 = Student()
s1.setgroup("CSC", "pass")
s1.getdetails()