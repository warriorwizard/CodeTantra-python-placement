import sys
import bisect
'''This program prints the longest ascending se quence(as a array)
in a given array'''
import array as arr
# L1 is a array of integer elements scanned speparated with spaces
L1=arr.array('i',[int (x) for x in input("Please enter a list of numbers separated by space: ").split()])
print(L1)
def longest(nums):
	sub=[]
	for i in range(len(nums)):
		temp=nums[i:]
		val=[]
		max=-9999
		for i in temp:
			if i>max:
				val.append(i)
				max=i
		sub.append(val)
	sub.sort(key=len)
	m=len(sub[-1])
	for i in sub:
		if len(i)==m:
			return i
	# return sub[-1]
a=longest(L1)
L2=arr.array('i',a)
print(L2)
		

