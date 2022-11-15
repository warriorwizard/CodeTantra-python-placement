
str1=input("str: ")
a=str1.startswith('Python')
b=str1.endswith('programming')
if str1.startswith('Python') and str1.endswith('programming'):
	print("valid")
else:
	print("invalid")
print("character with min val:",min(str1))
print("character with max val:",max(str1))