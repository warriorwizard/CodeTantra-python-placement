import array as arr
n = int(input("Enter size of the array : "))
a = arr.array('i',[])
print("Enter array elements : ")
for i in range(n):
	r=int(input())
	a.append(r)
a[0],a[-1]=a[-1],a[0]
print("After swapping the array elements : ")
for i in a:
	print(i,end=' ')
"""
Write remaining logic of the code.
Use array a for input and printing results

"""
