data=list(map(int,input("data: ").split(',')))
print("list:",data)
print("sum:",sum(data))
res=[i**2 for i in data]
print("squares:",res)
print("sum of squares:",sum(res))