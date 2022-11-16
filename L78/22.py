m=int(input("Number of rows, m = "))
n=int(input("Number of columns, n = "))
final=[]
for i in range(m):
	temp=[]
	for j in range(n):
		k=int(input(f'Entry in row: {i+1} column: {j+1}\n' ))
		temp.append(k)
	final.append(temp)
print(final)
# print()