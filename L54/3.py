from collections import Counter

def frequency (seq):
	b=seq.copy()
	a=Counter(b)
	mini=9999
	maxi=-9999
	for i in set(b):
		if a[i]<mini:
			mini=a[i]
		if a[i]>maxi:
			maxi=a[i]
	min_lis=[]
	max_lis=[]
	for i in set(b):
		if a[i]==mini:
			min_lis.append(i)
		if a[i]==maxi:
			max_lis.append(i)
	return (sorted(min_lis),sorted(max_lis),mini,maxi)
	
	
	
	
	# write your code here
		
	
	
	
	
	
l1 = [int(x) for x in input("Please enter integers separated by spaces: ").split()]
print (frequency(l1))