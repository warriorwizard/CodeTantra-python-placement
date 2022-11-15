a=list(map(int,input('data1: ').split(',')))
b=list(map(int,input('data2: ').split(',')))
c=list(map(int,input('data3: ').split(',')))
d=list(map(int,input('data4: ').split(',')))
e=dict(zip(a,b))
f=dict(zip(c,d))
for i in f.keys():
	if i in e.keys():
		e[i]+=f[i]
	else:
		e[i]=f[i]
print('concatenation:',list(sorted(e.items())))