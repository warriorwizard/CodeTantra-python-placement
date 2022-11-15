a=input('data: ').split(',')
print('tuple:',tuple(a))
e=input('element: ')

if e in a:
	print('index:',a.index(e))
else:
	print('enter an element that exists in tuple')