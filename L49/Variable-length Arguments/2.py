#Program to illustrate variable number of arguments
def mySum(*args):
	sum=0
	for i in args:
		sum+=i
	return sum

#Write your code here

print(mySum(1, 2, 3, 4, 5, 6, 7))	#7 arguments
print(mySum(1, 2))	#2 arguments
print(mySum(1, 2, 3))	#3 arguments