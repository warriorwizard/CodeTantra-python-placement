import math
num = float(input("num: "))
if num - int(num) >=.5:
	print ("result:", math.ceil(num))
else:
	print("result:", math.trunc(num))