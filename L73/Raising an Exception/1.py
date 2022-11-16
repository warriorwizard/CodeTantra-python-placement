def checkage(age):
	if age < 0:
		raise ValueError("age should be greater than or equal to zero")
	print("age is valid")
# write your code here
try:
	age=int(input("age: "))
	checkage(age)
except ValueError:
	print("('age should be greater than or equal to zero',)")
finally:
	print("executed in any condition")
