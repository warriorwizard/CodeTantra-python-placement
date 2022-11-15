a=input('data1: ').split(',')
b=input('data2: ').split(',')
e=dict(zip(a,b))
c=input('data3: ').split(',')
d=input('data4: ').split(',')
f=dict(zip(c,d))
key=input('key: ')
if (key in e.keys()) and (key in f.keys()):
	print('key present in both dictionaries')
elif key in e.keys():
	print('key present in first dictionary')
elif key in f.keys():
	print('key present in second dictionary')
else:
	print('key is not present')