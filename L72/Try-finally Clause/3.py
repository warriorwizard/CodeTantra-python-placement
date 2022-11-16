try:
	a=int(input("a: "))
	b=int(input("b: "))
	c=a+b
	d=a/b
	print(f'try successful {c} {d}')
except Exception:
	print("exception occurred")
finally:
	print("executed in any condition")
	