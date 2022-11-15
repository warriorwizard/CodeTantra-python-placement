# a=[]
b=input("data: ").split(',')
# a.append(b)
print('list:',b)
a=int(input('index: '))
try:
	print('element:',b[a])
except:
	
	print('invalid')