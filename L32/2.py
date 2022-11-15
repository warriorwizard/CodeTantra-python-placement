str1 = input("str: ")
# make string str1 into all upper case letters.
st=str1.upper()
print(st)
# make string str1 into only every word of first letter into upper case.
st1=str1.title()
print(st1)

# split every word of a string str1 with space.
at2=str1.split(' ')
print(at2)
# fill str1 with '%' special characer 25 width
print(str1.center(25,'%'))
# make string str1 into small letters.
print(str1.lower())
str2 = '@'
# join string str2 with str1
a=str2.join(str1)
print(a)

# replace a word 'Strings' with 'Tuples'.
print(str1.replace("Strings" ,"Tuples"))