a=set(input("data1: ").split(','))
b=input("element to discard: ")
if b in a:
	a.discard(b)
	print("sorted set after discarding:",sorted(list(a)))
	k=input("element to remove: ")
	a.remove(k)
	print("sorted set after removing:",sorted(list(a)))
else:
	print("not in set")