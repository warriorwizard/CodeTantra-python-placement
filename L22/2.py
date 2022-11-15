# Python program to find the sum of integers between 0 and n where n is provided by user
n=int(input("num: "))
m=0

# while n>m:
# 	print("sum:",n*(n+1)//2)
# 	break
# if n==0:
# 	print("sum: 0")
if n<0:
	while n<0:
		m-=n
		n+=1
	m=-1*m
	print("sum:", m)
else:
	while n>0:
		m+=n
		n-=1
	print('sum:',m)
	 #break
	# while n<m:
	# 	print("sum:,n*(n+1)//2")