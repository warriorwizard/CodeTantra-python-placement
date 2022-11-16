n=int(input("Enter size of list: "))
res=[]
for i in range(n):
	val=int(input("Enter value: "))
	res.append(val)
print("Original List =",res)
print("Reversed List =",res[::-1])
	