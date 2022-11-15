a=input('data: ').split(',')
s=int(input('start index: '))
e=int(input('end index: '))
if s<len(a) and e<len(a) and (s>len(a)*-1 and e>len(a)*-1):
	print('tuple in given range:',tuple(a[s:e]))
else:
	print('enter valid index')