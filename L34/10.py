data=input("data: ").split(",")
print("before updation:",data)
index=int(input("index: "))
if index<len(data) and index>len(data)*-1:
	tmp=input("element: ")
	data[index]=tmp
	print('after updation:',data)
else:
	print('invalid')
