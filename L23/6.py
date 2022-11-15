#Program to print value of pi 1 to 25 decimals
import math
pi = math.pi
n=int(input("n: "))
for i in range(1,n+1):
	print('{:.{}f}'.format(pi,i))
# write your code here