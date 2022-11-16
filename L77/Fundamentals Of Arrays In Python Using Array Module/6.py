from array import *
arr=[[11,21,31,41],[81,91,101,121]]
print("Display elements before performing insertion in 2-D array : ")
print(arr)
arr.insert(1, [5,6,7,8])
print("Display elements after performing insertion in 2-D array :")
for i in arr:
	for j in i:
		print(j, end=" ")
	print()