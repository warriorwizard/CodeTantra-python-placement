matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print("matrix:")
print(matrix)
# write your code here
# print("transposition using nested while:")
# res=
print("transposition using nested while:")
rez=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(rez)
print("transposition using nested for:")
print(rez)
print("transposition single list comprehension:")
print(rez)
print('transposition double list comprehension:')
print(rez)