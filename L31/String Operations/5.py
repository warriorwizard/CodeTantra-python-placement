str1=input("str: ")
# str1[0],str1[-1]=str1[-1],str1[0]
# a=str1[::-1]
# print(a)
# b=a[1:5]
# l=b[::-1]
# print(l)
# # c=b[::-1]
if len(str1)==0:
	print("null")
elif len(str1)==1:
	print(str1)
else:
	val=str1[::-1]
	res=str(val[0]+val[1:-1][::-1]+val[-1])
	print("output:",res)