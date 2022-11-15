s=input("str: ")
n=int(input("num: "))
if n>=len(s) or n<0:
	print("num should be positive, less than the length of str")
# elif 
else:
	print(f"output:",s[:n]+s[n+1:])
	