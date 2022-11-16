a=(input("Please enter a string: "))
b=(input("Please enter another string: "))
if len(a)==len(b):
	print("Strings are of equal Length")
	print("True")
elif len(a)-len(b)==1:
	print("Some Character is extra in string1")
	print('Strings after removal of the extra character: %s %s'%((a[:1]+a[2:]),b))
	print("False")
elif len(b)-len(a)==1:
	print('Some Character is extra in string1')
	print('Strings after removal of the extra character: %s %s'%((b[:1]+b[2:]),a))
	print('False')
else:
	print('Lengths differ by more than 1')
	print("False")
