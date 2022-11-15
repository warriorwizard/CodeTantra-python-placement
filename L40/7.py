a=input('data1: ').split(',')
b=input('data2: ').split(',')
dic1= dict(sorted(zip(a,b)))
dic2=dict(sorted(zip(b,a)))
print('dictionary with key order')
for i,j in dic1.items():
	print(i,j)
print('dictionary with value order')
for i,j in dic2.items():
	print(i,j)
