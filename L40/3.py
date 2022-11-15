
troupe = {('Cleese', 'John') : [1, 2, 3],
			('Chapman', 'Graham') : [4, 5, 6],
			('Idle', 'Eric') : [7, 8, 9],
			('Jones', 'Terry') : [10, 11, 12],
			('Gilliam', 'Terry') : [13, 14, 15, 16, 17, 18],
			('Palin', 'Michael') : [19, 20]}
for i,j in sorted(troupe.items()):
	a=(list(i))
	print(f"{a[1]} {a[0]} {j}")
