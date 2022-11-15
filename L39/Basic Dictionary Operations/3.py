a=input('data1: ').split(',')
b=input('data2: ').split(',')
if len(a)==len(b):
	print(sorted(list(zip(a,b))))
else:
	print('length should be equal')