def simplecalc(a, b = 100):
	print('addition:',a+b)
	print('subtraction:',a-b)
	print('multiplication:',a*b)
	
num1=int(input('num1: '))
num2=int(input('num2: '))
simplecalc(a = num1)
simplecalc(b = num2, a = num1)