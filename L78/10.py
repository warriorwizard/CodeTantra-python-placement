size=int(input("Enter size of int-list: "))
st=int(input("Enter size of string-list: "))
res=[]
for i in range(1,size+1):
	a=int(input("Enter int for int-list: "))
	res.append(a)
res1=[]
for j in range(1,st+1):
	b=(input("Enter string for string-list: "))
	res1.append(b)
dic={}
t=dict(zip(res,res1))
print(t)
