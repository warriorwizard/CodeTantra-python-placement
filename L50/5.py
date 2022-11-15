a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 6, 7, 9, 8]
# apply lambda function to the filter function and print the result
print(list(filter(lambda x: x in a,b)))
# print the result using list comprehension
print([x for x in a if x in b]) 
# follow the example given in description