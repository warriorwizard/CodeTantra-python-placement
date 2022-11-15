n=int(input('rows: '))
from math import factorial

for i in range(n):
	for j in range(n-i):
		print(end=" ")
	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
	print()