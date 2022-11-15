mytup = ('a', 'b', 'c', 'd', [1, 2, 3])
print("mytup =", mytup)
print("del mytup[4][2]")

# delele the element 3 from the mytup
del mytup[4][-1]
print("mytup =", mytup)
print("del mytup[4] will give TypeError")