from collections import Counter
a=list(input('Please enter a sentence: ').lower())
b=Counter(a)
c=list(set(a.copy()))
c.sort()
for i in c:
	if i.isalpha():
		print(str(i)+" 	 "+str(b[i]))