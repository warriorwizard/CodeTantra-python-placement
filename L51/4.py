def computeGCD(x, y):


# write your code here
	while(y):
		x,y=y,x%y
	return x
x=int(input("x: "))
y=int(input("y: "))
print(computeGCD(x,y))a