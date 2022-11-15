n=int(input("n1: "))
n2=int(input("n2: "))
my_set = {i**2 if i % 2 == 0 else i**3 for i in range(n,n2)}
	
print(sorted(list(my_set)))