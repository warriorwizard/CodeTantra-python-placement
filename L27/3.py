n=int(input('n: '))
l=len(str(n))
sum=0
a=n*1
while n>0:
	temp=n%10
	n=n//10
	sum+=temp**l
print('sum of powers:',sum)
if sum==a:
	print('armstrong number')
else:
	print('not armstrong number')