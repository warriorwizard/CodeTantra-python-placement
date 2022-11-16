import array as arr
a = arr.array('i',[])
n = int(input("Enter size of the array : "))
print("Enter array elements : ")

flag0=False
flag1=False
flag2=False
for i in range(n):
	k=int(input())
	if k==1:
		flag0=True
	elif k==2:
		flag1=True
	elif k==3:
		flag2=True
	# a.append(k)
# for i in range(n):
# 	if a[i]==1 and a[i]==2 and a[i]==3:
if flag0==True and flag1==True and flag2==True:
	print("true")
	# elif a[i]!= 1 and a[i]!= 2 and a[i]!=3:
else:
	print("false")
	# break
