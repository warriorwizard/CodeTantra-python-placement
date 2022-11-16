def dups(list1):

	_size=len(list1)
	final=[]
	out = []
	# for i in range(_size):
	# 	k=i+1
	# 	for j in range(k,_size):
	# 		if list1[i]==list1[j] and list1[i] not in repeated:
	# 			repeated.append(list1[i])
	# return repeated
	for i in list1:
		if i not in final:
			final.append(i)
		else:
			out.append(i)
	return out





list1 = []	#List declaration
n = int(input("Enter size of list: "))
for i in range(n):
	value = int(input("Enter value: "))
	list1.append(value)



print("Original List =", list1)
print("Duplicates =", dups(list1))