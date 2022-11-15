# Write your code here
k=int(input("k: "))
# a,b=0,1
lis=[0,1]
a=0
b=1

while b<=k:
	# print(b)
	a=a+b
	if a<k:
		lis.append(a)
	b=b+a
	if b<k:
		lis.append(b)
for i in lis:
	print(i)
val=sum(lis[::2])
print('sum:',val)
	# print(b)