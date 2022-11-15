def cal(salary,percent=20):
	tax=salary*percent/100
	print(tax)
	# print(tax)
salary=float(input('salary: '))
per=float(input('tax percentage: '))
cal(salary)
cal(salary,per)