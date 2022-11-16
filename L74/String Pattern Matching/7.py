import re
string=input("string with email address: ")
val=re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+)',string)
if len(val)>0:
	print('email address:',val)
else:
	print('No email address found')