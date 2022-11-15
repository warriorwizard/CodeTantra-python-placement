n=int(input('num: '))
if n<0:
	print('enter a positive value')
else:
	def fact(n):
		if n==1:
			return 1
		else:
			return n*fact(n-1)
	val=fact(n)
	print(f'factorial of {n} is: {val}')