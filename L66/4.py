class Greeting:
	def sayHello(self, name = None, wish = None):
		if name is not None and wish is not None:
			print ('Hello' + name + wish)
		elif name is not None and wish is None:
			print ('Hello' + name)
		else:
			print ('Hello')
greet = Greeting()
# Call the method with zero, one and two parameters
greet.sayHello()
greet.sayHello('Ram')
greet.sayHello('Ram,', 'Good Morning!!!')