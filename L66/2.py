class Person:
	pass
	def setName(self,name):
		self.name=name
	def getName(self):
		return self.name
p1=Person()
p2=Person()
p1.setName(input('p1 name: '))
p2.setName(input('p2 name: '))
print('p1 name:',p1.getName())
print('p2 name:',p2.getName())