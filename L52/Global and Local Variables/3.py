#Program to illustrate Global and Local Variables

# take input a from the user
a=int(input("a: "))
def changeglobal():
	global a
	a = 200
def changelocal():
	a = 500
	print("local a value:", a)
print("global a before function call:", a)
# call the function changeglobal
changeglobal()
changelocal()
# call the function changelocal
print("global a after function call:", a) # print value of a here