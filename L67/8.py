class vehicle:
	def __init__(self,name,price,regno):
		self.name=name
		self.price=price
		self.regno=regno
# write your code here


class car(vehicle):
	''' Class car inherits from Vehicle'''
	def __init__(self,name,price,regno,gear):
		self.name=name
		self.price=price
		self.regno=regno
		self.gear=gear
# write your code here

class boat(vehicle):
	''' Class boat inherits from vehicle'''	
	pass
# write your code here
	
class hover(car, boat):
	'''Class hovercraft inherits from both car and boat'''
	pass
c1 = car('toyota', 1500000, 'car2121', 'auto')
b1 = boat('maruti', 1000000, 'boat0121')
h1 = hover('toyota', 1500000, 'hover1212', 'manual')
print(type(c1).__name__, "\t", c1.name, "\t", c1.price, "\t", c1.regno, "\t", c1.gear)
print(type(b1).__name__, "\t", b1.name, "\t", b1.price, "\t", b1.regno, "\t")
print(type(h1).__name__, "\t", h1.name, "\t", h1.price, "\t", h1.regno, "\t", h1.gear)
print(c1.__doc__)