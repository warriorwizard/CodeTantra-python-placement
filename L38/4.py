a=input('data: ').split(',')
print('tuple:',tuple(a))
e=input('element: ')
if e in a:
	print('existed '+str(a.count(e))+ " times")
else:
	print('enter valid element')