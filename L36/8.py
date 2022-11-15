sd=input('Please enter A in upper case: ')
df=input('Please enter A in lower case: ')
i=ord('A')
j=ord('a')
a=[]
for k in range(26):
	a.append(chr(i))
	a.append(chr(j))
	i+=1
	j+=1
print(a)