a=input('data: ').split(',')
print('list:',a)
print('tuple:',tuple(a))
i=int(input('index: '))
if i <len(a) and i>len(a)*-1:
	print('element:',a[i])
else:
	print('enter valid index')
