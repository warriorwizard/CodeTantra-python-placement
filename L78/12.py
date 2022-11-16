a=input('Enter file name: ')
b=open(a,'r')
c=b.readlines()
c=c[::-1]
for i in c:
	print(i.rstrip())