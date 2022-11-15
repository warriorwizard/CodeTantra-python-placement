# Take an integer input from the user
n=int(input('n: '))
if(n<51):# write your condition here
	for i in range(1, n + 1):
		# print the numbers
		print(i,end=" ")
		#otehrwise print Enter a valid value (1 - 50)
else:
	print('enter valid value')