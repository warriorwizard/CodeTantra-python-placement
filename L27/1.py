n=int(input('n: '))

def fibbo(n):
	if n<=1:
		return n
	return fibbo(n-1)+fibbo(n-2)
if n<0:
	print('enter positive number: ')
elif n==0:
	print(0)
else:
	for i in range(2*n):
		val=fibbo(i)
		if val>n:
			break
		else:
			print(fibbo(i))