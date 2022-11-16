class Person:
	pass
	def setname(self,name):
		self.name=name
	def getname(self):
		return self.name
a=Person()
b=Person()
a.setname(input('name1: '))
b.setname(input('name2: '))
print(a.getname())
print(b.getname())