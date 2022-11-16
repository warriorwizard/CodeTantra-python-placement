class Employee:
	def __init__(self, name, salary):
		self.name=name
		self.salary=salary
		
		
	def displayEmployee(self):
		print('name:',self.name,', salary:',self.salary)

a=input('name: ')
b=input('salary: ')
emp=Employee(a,b)
emp.displayEmployee()
		
# Print the details of the employee