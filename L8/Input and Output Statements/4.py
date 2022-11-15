# Take an integer input from the user and store it in variable "a"
a=int(input("a: "))
# Take an integer input from the user and store it in variable "b"
b=int(input("b: "))
# print "a" value at 0 index and "b" value at 1 index
print(f"The value of a = {a}, b = {b} ")
# print by changing the index postions of "a" and "b" and observe the output
a,b=b,a
print(f"The value of a = {a}, b = {b} ")