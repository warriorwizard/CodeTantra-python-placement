a=input('data1: ').split(',')
b=input('data2: ').split(',')
for i,j in dict(sorted(zip(a,b))).items():
	print(str(i)+' -> '+str(j))