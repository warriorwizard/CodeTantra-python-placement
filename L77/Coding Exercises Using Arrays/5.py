import array as arr
a = arr.array('i',[])
n = int(input("Enter size : "))
print("Enter elements : ")

'''
Complete your code here
Use array a using array package imported above
'''
for i in range(n):
	k=int(input())
	a.append(k)
l=int(input("Enter an integer value : "))
def count(first,l):
	count=0
	for ele in a:
		if (ele==l):
			count=count+1
	return count
print(l," is repeated ",count(a,l), " times")
			# break