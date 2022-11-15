# Write your code here
str1=input("str: ")
tmp=""
for i in range(1,len(str1)+1):
	tmp+=str1[:i]
	# print(tmp)
	# for j in tmp:
print("incremental order:",tmp)