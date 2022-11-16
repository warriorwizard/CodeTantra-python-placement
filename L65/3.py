class Student:
	def __init__(self, name, age, email):
		self.name=name
		self.age=age
		self.email=email
		
	def studentDetails(self):
		print('name:',self.name,', age:',self.age,', email:',self.email)
a=input('name: ')
b=int(input('age: '))
c=input('email: ')
st=Student(a,b,c)
st.studentDetails()
		

