str1=input("str: ")
num=int(input("num: "))
a=str1[:num]
if num<0:
	print("num should be positive, less than length of str")
else:
	print("result:",a*num)
