def largestintwo(num1,num2):
	if num1>num2:
		return num1
	else:
		return num2
	
	
# write your code here	
	
num1=int(input("num1: "))
num2=int(input("num2: "))

result = largestintwo(num1, num2)
print("largest:", result)