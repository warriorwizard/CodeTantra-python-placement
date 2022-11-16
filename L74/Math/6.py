import math
xinrad = int(input("num: "))
x = math.pi / xinrad
print("arc cosine:",math.acos(x))
# print the arc sine value
print("arc sine:",math.asin(x))
#  print the arc tan value

print("arc tangent:", math.atan(x))
print("cosine:",math.cos(x))
print("sine:",math.sin(x))
print("tangent:",math.tan(x))

# Retrun the sine of x
# Retrun the tan of x
a = int(input("a: "))
b = int(input("b: "))

# Return the value of atan(y / x), in radians.
print(f'value of atan2({b}, {a}): {math.atan2(b,a)}')
print(f'value of hypot({a}, {b}): {math.hypot(a,b)}')
# Returns the Euclidean norm of given two numbers