from datetime import datetime
import time

import datetime

from datetime import date

import locale

#Taking input date from the user and convert into int formate using datetime object
year,month,day=input("date in yyyy-mm-dd format: ").split('-')
x=date(int(year),int(month),int(day))
print('date, time in locale format:',x.strftime("%c"))
print("weekday in locale format:",x.strftime("%a"))
print('date in locale format:',x.strftime('%x'))
# print Date and Time in locale formate
# d=time.strftime("%c")
# print("date, time in locale format:",d)



# print the Weekday in locale formate

# print Date in locale formate



