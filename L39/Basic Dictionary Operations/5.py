a=input('data1: ').split(',')
b=input('data2: ').split(',')
key=input('key: ')
dic=dict(zip(a,b))
if key in dic:
	print('True')
else:
	print('False')