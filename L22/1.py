num=int(input("num: "))
total=0


while num>0:
		if num%2==0:
			total+=num
			num-=1
		else:
			num=num-1
print("sum:",total)

# elif num==0:
# 	print("sum: 0")
# else:
# 	print("sum")
	