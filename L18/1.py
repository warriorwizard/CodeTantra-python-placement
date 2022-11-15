num=int(input('num: '))
lis=[]
for i in range(1,(num//2)+1):
	if num%i==0:
		lis.append(i)
print('factors:',lis)
print('sum:',sum(lis))
if sum(lis)==num:
	print('perfect number')
elif sum(lis)>num:
	print('abundant number')
else:
	print('deficient number')