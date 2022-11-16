from datetime import datetime
from datetime import date
year,month,day=input("date in yyyy-mm-dd format: ").split('-')
x=date(int(year),int(month),int(day))
print('date:',x)
print(f'month:',int(month),',day:',int(day),',year:',int(year) )
year1=int(input('year before/after the current year: '))
if year1>int(year):
	print(year1-int(year),'years after the current year')
else:
	print(int(year)-year1,'years before the current year')
# print("year before/after the current year:")
# print(f' years before the current year')
