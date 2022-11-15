a=list(input("data: ").split(','))
b=a
print('list1 is list2:',a is b)
print('list2 is list1:',b is a)
i=int(input("index: "))
if i<len(a) and i>=len(a)*-1:
	val=input('element: ')
	a[i]=val
	print('list1 is list2:',a is b)
	print('list2 is list1:',b is a)
else:
	print('enter valid index')