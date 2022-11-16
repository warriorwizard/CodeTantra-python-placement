def fibbo(n):
	lis=[0,1]
	a=0
	b=1
	count=2
	while True:
		a=a+b
		if count<n:
			lis.append(a)
			count+=1
		else:
			break
		b=a+b
		if count<n:
			lis.append(b)
			count+=1
		else:
			break
	return lis
def prime(n):
	if n<2:
		return False
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True
n=int(input("Enter an integer value: "))
val=fibbo(n)
print("Fibonacci numbers:",val)
sum=0
final=[]
for i in val:
	if prime(i)==True:
		sum+=i
		final.append(i)
print("The prime numbers of fibonacci series:",final)
print("The sum of the prime numbers:",sum)
# for i in a