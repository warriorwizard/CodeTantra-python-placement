#Program to illustrate Variable number of arguments
def largestNumber( * numbers):
	print("largest: "+str(max(numbers)))
	# return a

# write your code here



largestNumber(1, 2, 3, 4)			#4 arguments
largestNumber(8, 9, 3, 4, 2, 5)		#6 arguments