from array import *
arr=[[10,20,30],[40,50,60],[70,80,90]]
print("Array before modification")
for _ in arr:
	for i in _:
		print(i,end=" ")
	print()
arr[1].insert(2,120)
print("Array after modification")
for _ in arr:
	for i in _:
		print(i,end=" ")
	print()