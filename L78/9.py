a=input("Enter strings contained name and dob with : seperated\n").split()
dic=dict()
for i in a:
	val=i.split(':')
	dic[val[0]]=val[1]
print("The list:",a)
fin="---".join(a)
print('The list with join:',fin)
print('The sorted dictionary:',sorted(dic.items()))
# k=e.split(',')
# print(e)
