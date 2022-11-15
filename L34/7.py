data=input("data1: ").split(",")
data1=input("data2: ").split(",")
num=int(input("num: "))
tmp=data+data1
data=data*num
data1=data1*num
print(data)
print(data1)
print('extending list1 with list2:',tmp)