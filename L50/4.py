def squares(x):
	return x ** 2
list1 = [1, 2, 3, 4, 5]
#use the squares func inside map function print the result
print(list(map(squares,list1)))

#use the lambda func inside map function print the result
print(list(map(lambda x: x**2,list1)))
#use list comprehension to get equivalent behaviour as map and print the result
print([x**2 for x in list1])