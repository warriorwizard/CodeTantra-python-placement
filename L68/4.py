class Animal:
	def __init__(self,name="Rabbit"):
		self.name=name
	def eat(self,food="Grass"):
		print(self.name,"eats",food)
class Mammal(Animal):
	def __init__(self,name):
		self.name=name
	def eat(self):
		print(self.name,"does not eat. It only drinks")
class WingedAnimal(Animal):
	def __init__(self,name):
		self.name=name
	def eat(self):
		print(self.name,"eats anything and everything")
class Bat(WingedAnimal):
	def smell(self):
		print(self.name,"The Animal Stinks")
class FruitBat(Mammal, WingedAnimal):
	
	pass
	rabbit1=Animal()
	print("Rabbit1 is an instance of Animal")
	rabbit1.eat()
	rabbit1.eat("Peanuts")
	print('Cow1 is an instance of Mammal')
	cow1=Mammal('Cow')
	cow1.eat()
	print('Vulture1 is an instance of WingedAnimal')
	vulture1= WingedAnimal('Vulture')
	vulture1.eat()
	print('Bat1 is an instance of Bat')
	bat1=Bat('Bat')
	bat1.eat()
	print('fbat is an instance of FruitBat')
	fbat=Mammal('Fruitbat')
	fbat.eat()
	# print("Fruitbat")