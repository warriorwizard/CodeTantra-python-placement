a=input('seq: ').split(',')
b={}
c=list(set(a.copy()))
for i in c:
	temp=a.count(i)
	b[int(i)]=temp
print('sorted dictionary:',list(sorted(b.items())))