#Program to combine two dictionaries
data1 = input("Enter integer elements separated by ,(comma) for keys of dict1: ")
data2 = input("Enter integer elements separated by ,(comma) for values of dict1: ")
list1 = data1.split(",")
list2 = data2.split(",")
for i in range(len(list1)):
	list1[i] = int(list1[i])
	
for i in range(len(list2)):
	list2[i] = int(list2[i])
dict1 = dict(zip(list1, list2))

data3 = input("Enter integer elements separated by ,(comma) for keys of dict2: ")
data4 = input("Enter integer elements separated by ,(comma) for values of dict2: ")
list3 = data3.split(",")
list4 = data4.split(",")
for i in range(len(list3)):
	list3[i] = int(list3[i])
	
for i in range(len(list4)):
	list4[i] = int(list4[i])
dict2 = dict(zip(list3, list4))

dict3 = {}
for i in dict1.keys():
	if i in dict2.keys():
		dict3[i]=dict1[i]+ dict2[i]
	else:
		dict3[i]=dict1[i]
for i in dict2.keys():
	if i not in dict3.keys():
		dict3[i]=dict2[i]
print(list(sorted(dict3.items())))

