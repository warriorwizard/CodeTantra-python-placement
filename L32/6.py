#use len() to find length of String
str1=input("str1: ")
str2=input("str2: ")
# if len(str1)>len(str2):
# 	print(str2+str1+str2)
if len(str1)==len(str2):
	print("strings are same length")
else:
	if len(str1)>len(str2):
		print(str2+str1+str2)
	else:
		print(str1+str2+str1)