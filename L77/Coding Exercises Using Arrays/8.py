import array as arr
def valley(l):

    if (len(l)<3):
    	return False
    up_count =1
    low_count =1
    for i in range(0, len(l)-1):
    	if l[i]>l[i+1]:
    		if low_count >1:
    			
    			return False
    		up_count = up_count +1
    	if l[i] <l[i+1]:
    		low_count = low_count+1
    	if l[i]==l[i+1]:
    		return False
    if up_count>1 and low_count > 1:
    	return True
    else:
    	return False
    
    
'''
Write your driver code to scan array with space separated elements
Write code to print the array

'''
lst=arr.array('i',[int(x) for x in input("Input Integers separated by spaces: ").split()])
# ("Input Integers separated by spaces: "))
print("Entered array is: ",lst)
# for i in range(len(k)):
# 	ls1.append(k)
# lst.append(val)
# print("Entered array is:",lst)
print(valley(lst))