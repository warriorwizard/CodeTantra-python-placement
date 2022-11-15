x=int(input('x: '))
y=int(input('y: '))
def isprime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True
for i in range(x,y):
	if isprime(i):
		print(i)