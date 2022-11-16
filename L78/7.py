def fibbo(n):
	lis=[0,1]
	a=0
	b=1
	while True:
		a=a+b
		if a<n:
			lis.append(a)
		else:
			break
		b=a+b
		if b<n:
			lis.append(b)
		else:
			break
	return lis
k=int(input("Enter an integer: "))
val=fibbo(k)
sum=0
for i in range(len(val)):
	if val[i]%2==0:
		sum+=val[i]
print("The sum of even numbers of fibonacci sequence",val,'is:',sum)