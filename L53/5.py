#Program to add two numbers using recursion
def add(x, y):
	if y==0:
		return x
	a=add(x,y-1)+1
	return a
a=int(input("a: "))
b=int(input("b: "))


	
	
# write your code here
	
		

	

print(add(a, b))