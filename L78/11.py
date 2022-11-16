a=input('Enter the filename: ')
b=input('Enter the character to be searched: ')
c=open(a,'r')
count=0
d=c.read()
for i in d:
	if i==b:
		count+=1
print(b,'appears',count,'times in file')
print('The type of file:',type(c))