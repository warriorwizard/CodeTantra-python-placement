#Program to illustrate keyword parameters
def simplecalc(a=3,b=4):
	print('addition:',a+b)
	print('subtraction:',a-b)
	print('multiplication:',a*b)

#define your function here and perform arithmetic operations addition, subtraction, multiplicateion and print the result.

simplecalc(a = 3, b = 5)
simplecalc(b = 4, a = 5)
#This function can also be called with positional arguments
simplecalc(8, 4)