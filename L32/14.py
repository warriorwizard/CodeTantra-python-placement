#Write your code her
str1=input("str: ")
if str1=="":
	print("null")
	print("first: ")
	print("second: ")
	print("original: ")
elif len(str1)==1:
	print(str1)
	print("first:",str1)
	print("second: ")
	print("original:",str1)
else:
	# print(str1)
	print("first:",str1[::2])
	print("second:",str1[1::2])
	print("original:",str1)
