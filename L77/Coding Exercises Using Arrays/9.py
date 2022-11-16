# Type you complete solution to run the test cases
a,b=map(int,input('Enter row and column sizes : \n').split())
print('Enter ',a*b,' values :')
c=[]
e=[]
for i in range(a):
	d=(list(map(int,input().split())))
	f=max(d)
	c.append(f)
	e.append(d)
print("The given matrix is")
for i in e:
	for j in i:
		print(j,end=" ")
	print()
for i in range(len(c)):
	print('Largest of row - ',i,' elements = ',c[i])