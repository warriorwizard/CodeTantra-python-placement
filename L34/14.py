data=list(input("data1: ").split(','))
data2=list(input("data2: ").split(','))
if data[0]==data2[0] or data[-1]==data2[-1]:
	print("True")
else:
	print("False")