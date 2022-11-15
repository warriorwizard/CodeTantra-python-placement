str1=str(input("str: "))
a=int(len(str1)//2)+1
# print(a)
# for i in range(a+1):
# 	print(str1(i))
# a=len()

if len(str1)%2==0:
	print("first half str of even length:",(str1[:len(str1)//2]))
else:
	
	print("second half str of odd length:",(str1[a:]))