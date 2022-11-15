a=input('data: ').split(',')
ind=int(input('index: '))
# val=input()
if ind<len(a) and ind>=len(a)*-1:
	val=input('value: ')
	a[ind]=val
	print('tuple:',tuple(a))
else:
	print('enter valid index')
