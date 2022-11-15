a=set(input("data1: ").split(','))
b=set(input("data2: ").split(','))
print("set1 sorted:",sorted(list(a)))
print("set2 sorted:",sorted(list(b)))
print("difference using difference():",sorted(list(a.difference(b))))
li=a.difference(b)
print("difference using difference_update():",sorted(list(li)))
print("difference using (set1 - set2):",sorted(list(a-b)))
k=a-b
print("difference using (set1 -= set2):",sorted(list(k)))

