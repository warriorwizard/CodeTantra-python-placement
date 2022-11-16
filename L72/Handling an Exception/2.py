try:
	a=int(input("a: "))
	b=int(input("b: "))
	c=a+b
	d=a*b
	e=a/b
	print("try successful")
		
except ZeroDivisionError:
	# print here
	if b==0:
		print("zero division error occurred")
except NameError:
	# print here
	print("")
except Exception:
	# print here
	print("exception occurred")
