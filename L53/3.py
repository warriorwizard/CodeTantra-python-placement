#Program to illustrate recursion
def recurfact(n):
	if n==1:
		return n
	else:
		return n*recurfact(n-1)
num=int(input("num: "))
if num<0:
	print("factorial not exist for negative number")
elif num==0:
	print("factorial: 1")
else:
	print("factorial:",recurfact(num))
