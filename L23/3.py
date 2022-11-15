# Multiplication table
x = int(input("x: "))
y = int(input("y: "))

# Fill in the missing code below to print a multiplication table for x upto y rows.
# If y is more than 20, print the relevant message as per instructions and limit the number of rows to 20
if y<21:
	
	for i in range(1, y+1):
		print(f"{x} * {i} = {x*i}")
	

else:
	y=20
	for i in range(1,y+1):
		print(f"{x} * {i} = {x*i}")
	print("rows is limited to 20")
