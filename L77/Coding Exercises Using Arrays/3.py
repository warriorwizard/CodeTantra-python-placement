import array as arr
a = arr.array('i',[])
n = int(input("Enter size : "))
print("Enter elements : ")
'''
Write remaining code here
Use the array package imported

'''
# res=[]
for i in range(n):
	k=int(input())
	a.append(k)
# prin0t (res)
print("Enter an integer value : ")
l=int(input())
for i in range(n):
	if a[i]==l:
		print('Matching indexes:',i)
	
	