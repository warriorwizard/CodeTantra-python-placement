
data =list(input("data: ").split(','))
print(data)
# res=[*set(data)]
# b=sorted(res)
a=[i for j, i in enumerate(data) if i not in data[:j]]
print("after removing duplicates:",a)