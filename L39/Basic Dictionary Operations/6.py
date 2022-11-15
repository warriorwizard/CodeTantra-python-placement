a=input('data1: ').split(',')
b=input('data2: ').split(',')
dic=dict(sorted(zip(a,b)))
for i,j in dic.items():
	print(i,j)