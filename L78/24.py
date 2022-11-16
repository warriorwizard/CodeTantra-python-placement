print('Enter values for matrix - A')
a=int(input('Number of rows, m = '))
b=int(input('Number of columns, n = '))
A=[]
for i in range(a):
	temp=[]
	for j in range(b):
		k=int(input(f'Entry in row: {i+1} column: {j+1}\n'))
		temp.append(k)
	A.append(temp)
print('Enter values for matrix - B')
c=int(input('Number of rows, m = '))
d=int(input('Number of columns, n = '))
B=[]
for i in range(c):
	temp=[]
	for j in range(d):
		k=int(input(f'Entry in row: {i+1} column: {j+1}\n'))
		temp.append(k)
	B.append(temp)
print("Matrix - A =",A)
print("Matrix - B =",B)
if b!=c:
	print('Cannot multiply the two matrices. Incorrect dimensions.')
	print('Matrix - A * Matrix- B = None')
else:
	res=[[sum(a*b for a,b in zip(A_row,B_row)) for B_row in zip(*B)] for A_row in A]
	print("Matrix - A * Matrix- B =",res)
	