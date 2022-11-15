def valley(l):
	bol=0
	count=0
	for i in range(0,len(l)-1):
		if l[i+1]==l[i]:
			return False
		elif l[i+1]<l[i] and bol==0:
			count-1
		elif l[i+1]>l[i] and bol==0:
			bol=1
		elif l[i+1]< l[i] and bol==1:
			return False
	if bol== 0 and count==0:
		return False
	else:
		return True

l=list(input("integers space separated: ").split())
print(valley(l))
			
		
