import array as a
arr=a.array('i',[])
sum = 0
n = int(input()) 
for i in range(n): 
    # fill the required code here
    r=int(input())
    arr.append(r)
for i in arr:
# 	arr[i]+=arr[i]+1# Complete the missing code in the given for loop
    # fill the required code here
    sum+=i
print ('Sum of the array is ', sum)