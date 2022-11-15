a=input('data: ').split(',')
print('tuple:',tuple(a))
ind=int(input('index: '))
if ind<len(a) and ind>len(a)*-1:
	a.pop(ind)
	print('after removing:',tuple(a))
else:
	print('enter valid index')