a=input('data1: ').split(',')
b=input('data2: ').split(',')
c=dict(sorted(zip(a,b)))
key=input('key: ')
if key in c:
	val=c.pop(key)
	print('value:',val)
	print('dictionary:',list(c.items()))
else:
	print('key does not exist')