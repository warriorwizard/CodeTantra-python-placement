a=(input("temp with unit: "))
b=['F','C','f','c']
x=a[-1]
n=int(a[:-1])
if x in b:
	if x=='C' or x=='c':
		cal=(n/(5/9)+32)
		cal=round(cal,2)
		print(f'{n} C = {cal} F')
	elif x=='F' or x=='f':
		cal=(5/9)*(n-32)
		cal=round(cal,2)
		print(f'{n} F = {cal} C')
if x not in b:
	print('unrecognized unit:',x)