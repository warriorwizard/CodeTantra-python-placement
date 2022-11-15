list1=list(input("data1: ").split(','))
list2=list(input("data2: ").split(','))
if len(list1)==len(list2):
	res="{"
	for i in range(len(list1)):
		res+=("'"+str(list1[i])+"'")
		res+=":"
		res+=("'"+list2[i]+"'")
		res+=','
	res=res[:-1]
	res+='}'
	print(res)
	# k="}"
	# for i in list1:
	# 	for j in list2:
			# print(f'{list[i]}{i:j}{k}')
	# for key in list1:
	# 	for value in list2:
	# 		res[key]=value
	# 		list2.remove(value)
	# 		break
	# print((res))
else:
	print("lists are different lengths")
