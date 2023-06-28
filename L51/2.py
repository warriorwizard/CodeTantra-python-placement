def largestinthree(a, b, c):
	return max(a,max(b,c))
	# write your code here to find the largest number in a, b and c
		
num1 = int(input("Please enter a value for num1: "))
num2 = int(input("Please enter a value for num2: "))
num3 = int(input("Please enter a value for num3: "))

result = largestinthree(num1, num2, num3)

print("Largest of the values entered is", result)
