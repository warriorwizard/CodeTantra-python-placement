matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print('matrix:',matrix)
val=[[0]*len(matrix) for i in range(len(matrix[0]))]
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		val[j][i]=matrix[i][j]
print('transposed:',val)

# find the transpose of the matrix and print the result as shown in the example above