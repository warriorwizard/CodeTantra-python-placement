# take float number from the user
a=float(input('a: '))
# print up to 2 decimal points
print('{0:.2f}'.format(a))
# print up to 6 decimal points
print('{0:.6f}'.format(a))
# take int number from the user
b=int(input('Enter b value: '))
# print the number with one space
print(f'{b}')
# print the number with two spaces
print('{0:2}'.format(b))
# print the number with three spaces
print('{0:3}'.format(b))
# print the given number b in octal form
print(f'octal: {str(oct(b))[2:]}')
# print the given input b in hexadecimal form
val=str(hex(b))[2:]
print('hex:',val.upper())
	