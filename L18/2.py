
def getsum(num):
	s=0
	for digit in str(num):
		s +=int(digit)
	return s
num=int(input("num: "))
a=getsum(num)
print("sum:",a)