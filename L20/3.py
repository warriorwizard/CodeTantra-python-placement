# Deductions
Ded_std = 150000
# Request Inputs
Ded_80c = int(input("deduction under 80c: "))
Ded_80cc = int(input("deduction under 80cc: "))
Ded_hra = int(input("deduction under HRA: "))
Ded_med = int(input("deduction under Medical: "))
Gross_Income = int(input("gross income: "))
Ded_tot = (Ded_std + Ded_80c + Ded_80cc + Ded_hra + Ded_med)
Tax_Income = Gross_Income - Ded_tot
# Income_Tax=Tax_Income* 0.1
# complete the missing code
if Tax_Income>0:
	if Gross_Income <=500000:
		Income_tax=Tax_Income*.1
	if (Gross_Income <= 1000000) and (Gross_Income > 500000):
		Income_tax=25000+((Gross_Income - 500000)*.2)
	
	if(Gross_Income > 1000000):
		Income_tax = 75000+((Gross_Income - 1000000)*.3)
	print ("gross income" , Gross_Income)
	print ("total deductions =" , Ded_tot)
	print ("income tax =" , Income_tax)
else :
	print ("hurray..no income tax")