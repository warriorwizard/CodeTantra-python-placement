list1 = ["key1","key2","key3"]
list2 = ["value1","value2","value3"]
print(list1)
print(list2)
mydict = zip(list1,list2)	# using zip() function we can create dictionary with two lists(one list for keys and one list for values)

# convert dictionary into set using set() method
a=set(mydict)
# print elements in  sorted order
print(sorted(a))
# print(a)