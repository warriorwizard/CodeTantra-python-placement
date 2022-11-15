n=int(input("n: "))
factors=[]
for i in range(1,n//2+1):
	if n%i==0:
		factors.append(i)
print('factors:',factors)
if sum(factors)==n:
	print('perfect number')
else:
	print("not perfect number")
	