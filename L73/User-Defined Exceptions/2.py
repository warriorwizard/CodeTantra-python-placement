class OurException(Exception):
	# define constructor
	def __init__(self,message):
		self.message=message
	
	
class UsingUserException:
	try:
		a=int(input("a: "))
		b=int(input("b: "))
		if b==0:
			a="user defined exception: b should be greater than 0"
			print(OurException(a))
		else:
			c=a/b
			print("division operation successful with result:",c)
			
		
		#write code in try block
		
		
		
	except OurException as err:
		print("user defined exception:", err.message)