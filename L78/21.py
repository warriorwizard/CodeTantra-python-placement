def gcd(x,y):
	while(y):
		x,y=y,x%y
	return x
def lcm(x,y):
	lcm=(x*y)//gcd(x,y)
	return lcm
a=int(input("Enter an integer value: "))
b=int(input("Enter an integer value: "))
print(f"GCD of {a} and {b} is {gcd(a,b)}")
print(f'LCM of {a} and {b} is {lcm(a,b)}')