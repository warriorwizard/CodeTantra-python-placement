# write your code here
import re
mystring=input("data: ")
val=mystring.split(',')
match=re.search('(\w+),(\w+),(\w+),(\w+)',mystring)

# print(data)
if match and len(val)==4:
	print("full:",match.group())
	print("group 1:",match.group(1))
	print("group 2:",match.group(2))
	print("group 3:",match.group(3))
	print("group 4:",match.group(4))
else:
	print("you have not entered 4 words")