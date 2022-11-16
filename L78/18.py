def unique(list1):

#Write your code here...
	unique_list=[]
	for x in list1:
		if x not in unique_list:
			unique_list.append(x)
	return (unique_list)
		



list1 = []	#List declaration
n = int(input("Enter size of list: "))
for i in range(n):
	val = int(input("Enter value: "))
	list1.append(val)
	

#Write here....



print("Original List =", list1 )
# print("Unique elements =", unique(list1))
k=unique(list1)
print("Unique elements =",k)
 