# import array as arr
# a = arr.array('i',[])
# n = int(input("Enter size of the array :"))
# print("Enter array elements : ")

'''
write your solution here
use array package imported as arr
'''
import array as arr
a=arr.array('i',[])
n=int(input("Enter size of the array: "))
print("Enter array elements: ")
for i in range(n):
	k=int(input())
	a.append(k)
p=int(input("Enter an integer value: "))
if a[0]==p or a[-1]==p:
	print("true")
else:
	print("false")