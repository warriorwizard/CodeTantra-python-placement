a=set(input("data1: ").split(','))
b=set(input("data2: ").split(','))
c=set(input("data3: ").split(','))
print("set1 sorted:",sorted(list(a)))
print("set2 sorted:",sorted(list(b)))
print("set3 sorted:",sorted(list(c)))
print("is set1, set2 disjoint?",a.isdisjoint(b))
print("is set1, set3 disjoint?",a.isdisjoint(c))
print("is set2, set3 disjoint?",b.isdisjoint(c))
# print
# print