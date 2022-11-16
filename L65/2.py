class student:
	def __init__(self,name,age,email):
		self.name=name
		self.age=age
		self.email=email
a=input('s1 name: ')
b=input('s1 age: ')
Stud_1=student(a,b,'arya@gmail.com')
c=input('s2 name: ')
d=input('s2 age: ')
Stud_2=student(c,d,'geetha@gmail.com')
print('Stud_1.name:',Stud_1.name)
print('Stud_2.name:',Stud_2.name)