a=int(input("x: "))
b=int(input("y: "))
# if y==0 or x==0:
# 	print("value must be non zero")

def gcd(a,b):
	if a==0:
		return b
	else:
		return gcd(b%a,a)
		
# a=int(input("x: "))
if a==0 or b==0:
	print("value must be non zero")
else:
	val=gcd(a,b)
	print('gcd:',val)
	