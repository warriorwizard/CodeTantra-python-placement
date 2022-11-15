def add(x, y):
	# add x, y and print the result
	print(x+y)
def sub(x, y):
	# subtract x, y and print the result
	print(x-y)
def mul(x, y):
	# multiply x, y and print the result
	print(x*y)
	
# take inputs x and y from the user
# call the functions add,sub, mul 
a=int(input('x: '))
b=int(input('y: '))
add(a,b)
sub(a,b)
mul(a,b)