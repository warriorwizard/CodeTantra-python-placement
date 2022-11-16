try:
	a=int(input("a: "))
	b=int(input("b: "))
	c=a+b
	d=a/b
	print("try successful")
except ArithmeticError:
	print("arithmetic error occurred ") 
except Exception:
	print("exception occurred")
finally:
	print("executed in any condition")
