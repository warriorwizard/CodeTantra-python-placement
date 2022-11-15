#del
dlist = ['red', 'orange', 'blue', 'green', 'yellow', 'cyan']
print("dlist =", dlist)
print("del dlist[5]")
#delete element 5 
del dlist[5]
print("dlist =",dlist)
# print the result
print("del dlist[2:]")
del dlist[2:]
print("dlist =", dlist)
print("del dlist")
del dlist

#remove
remlist = ['red', 'orange', 'blue', 'green', 'yellow', 'cyan']
print("remlist =", remlist)
print("remlist.remove('green')")
remlist.remove("green")
print("remlist =",remlist)
# remove green from the list and print the list


#pop
plist = ['red', 'orange', 'blue', 'green', 'yellow', 'cyan']
print("plist =", plist)
print("elem = plist.pop(2)")

# remove element at index 2

print("element popped & removed :", plist[2])
plist.remove(plist[2])

print("plist =",plist )
print("elem = plist.pop()")
# elem=plist.pop(2)

# remove last element
# plist.remove(plist1[-1])
print("element popped & removed :", plist[-1])
plist.remove(plist[-1])
print("plist =", plist)
print("plist.clear()")
plist.clear()
print("plist =", plist)