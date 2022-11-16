m=int(input('Number of rows for matrix - A, m = '))
n=int(input('Number of columns for matrix - A, n = '))
p=int(input("Number of rows for matrix - B, p = "))
q=int(input("Number of columns for matrix - B, q = "))
if m!=p or n!=q:
	print("Addition is not possible")
else:
	print('Enter values for matrix - A')
	a=[]
	for i in range(m):
		temp=[]
		for j in range(n):
			k=int(input(f'Entry in row: {i+1} column: {j+1}\n'))
			temp.append(k)
		a.append(temp)
	print('Enter values for matrix - B')
	b=[]
	for i in range(p):
		temp=[]
		for j in range(q):
			k=int(input(f'Entry in row: {i+1} column: {j+1}\n'))
			temp.append(k)
		b.append(temp)
	print('Matrix a =',a)
	print('Matrix b =',b)
	res=[[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
	print('Addition of two matrices =',res)
	
