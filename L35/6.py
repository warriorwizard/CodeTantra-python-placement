# import numpy as np
data1=list(map(int,input("data1: ").split(',')))
data2=list(map(int,input("data2: ").split(',')))
# def diff(data1,data2):
# 	res=[i for i in data1+data2 if i not in data1 or i not in data2]
# 	return res
if len(data1)==len(data2):
	sub=list()
	for i, j in zip(data1,data2):
		res=i-j
		sub.append(res)
	print(sub)
		
else:
	print("lists are different lengths")