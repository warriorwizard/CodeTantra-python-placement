from array import *
arr=[[11,21,31,41],[81,91,101,121]]
print("Display elements before performing deletion's in 2-D array : ")
print(arr)
del(arr[0][2])
del(arr[1])
print("Display elements after performing deletion's in 2-D array :")
for i in arr:
	for j in arr:
		for j in i:
			print(j, end=" ")
		print()