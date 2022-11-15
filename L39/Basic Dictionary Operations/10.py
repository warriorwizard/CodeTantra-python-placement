a=input('data1: ').split(',')
b=input('data2: ').split(',')
key=input('key: ')
c=dict(sorted(zip(a,b)))
if key in c:
	val=input('value: ')
	val=c[key]=val
	# print('value:',val)
	print('sorted dictionary:',list(sorted(c.items())))
else:
	print('key does not exist')