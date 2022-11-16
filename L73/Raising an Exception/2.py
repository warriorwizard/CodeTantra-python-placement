try:
	age=int(input("age: "))
	if age<0:
		print("age should be greater than or equal to zero")
except Exception:
	print("age should be greater than or equal to zero")
except ValueError:
	print("age should be greater than or equal to zero")
finally:
	print("i am always executed")