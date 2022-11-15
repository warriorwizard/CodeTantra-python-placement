a=list(map(int,input('data1: ').split(',')))
b=list(map(int,input('data2: ').split(',')))
c=list(map(int,input('data3: ').split(',')))
d=list(map(int,input('data4: ').split(',')))
e=dict(zip(a,b))
f=dict(zip(c,d))
g={}
for i in e.keys():
	if i in f.keys():
		g[i]=e[i]+f[i]
print('common keys:',list(sorted(g.items())))