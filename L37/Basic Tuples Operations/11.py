a=input('data: ').split(',')
ele=input('element: ')
if ele in a:
	print('before deletion:',tuple(a))
	a.remove(ele)
	print('after deletion:',tuple(a))
else:
	print('enter existed element')