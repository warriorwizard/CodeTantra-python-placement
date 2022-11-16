def cumulative_product(list1):
	curr=1
	newlist=[]
	for i in list1:
		curr *= i
		newlist.append(curr)
		# return re.append(p)
	return newlist
		
	
#Write your code here...


n=int(input("Enter size of list: "))
res=[]
for i in range(n):

	k=int(input("Enter value: "))
	res.append(k)
	
# res=[]
# for j in k:
# 	res.append(k)

# n=int(input("Enter size of list: "))
print("Original List =",res)
print("Cumulative Product List =", cumulative_product(res))