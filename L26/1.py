#Program to illustrate the pass construct

numbers = [ 1, 2, 4, 3, 6, 5, 7, 10, 9 ]

#Check for each number that belongs to the list
for i in numbers:
	if i%2!=0:
		pass
	else:
		print(i)

	#check if the number is odd
	
	
			#if odd, then pass ( No operation )
			
		#print the even numbers