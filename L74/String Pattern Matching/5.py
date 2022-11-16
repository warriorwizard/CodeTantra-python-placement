import re
mystring = "Hello!! Good Morning, Welcome to python tutorial class 24.For any  queries please email to contactus@codetantra.com"

# write your code here
print(re.findall('^Hello',mystring))
print(re.findall(r'\d+',mystring))
p=re.compile('ac*|c')
print(p.findall(mystring))
