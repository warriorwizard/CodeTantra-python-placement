from collections import Counter
str1=input("str: ")
b=Counter(str1)
for i in b:
	print(f'{(i)} 	 {b[i]}')