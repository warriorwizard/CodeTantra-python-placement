a=int(input('a: '))
b=int(input('b: '))
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def ave(a,b):
	return (a+b)/2
def mul(a,b):
	return a*b
	
print(f"sum, average: ({add(a,b)}, {ave(a,b)})")
print('subtraction:',sub(a,b))
print('multiplication:',mul(a,b))
