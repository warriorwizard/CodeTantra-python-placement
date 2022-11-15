a=input('data: ').split(',')
b=input('seq of elements: ').split(',')
for i in b:
	if i not in a:
		print('does not exist')
		break
else:
	print('exist')