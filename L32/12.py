# write a program to print the every character in the given string twice'
str1=input("str: ")
# for s in str1:
def string1(s):
	double=''.join([i+i for i in s])
	return double
	# res=""
		# for i in str1:
			# res+=i*2
	# return res
print("result: ",string1(str1))