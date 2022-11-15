a=list(map(int,input('data: ').split(',')))
print('list:',a)
n=int(input('num: '))
for i in range(len(a)):
	if a[i]==n:
		if a[i+1]==n:
			print(True)
			break
else:
	print(False)