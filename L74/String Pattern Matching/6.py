import re
mystring = "Hello!! Good Morning, Welcome to python tutorial class 24."
matches = re.findall(r'eo*|oo*|o',mystring)# find all occcurences of e and o 

for m in matches:
	print(m)

# print m
