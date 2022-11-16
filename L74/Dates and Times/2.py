import datetime
from datetime import date
from datetime import timedelta
# Take the input date from the user in the form of yyyy-mm-dd and store it in a variable d
d=input("date in yyyy-mm-dd format: ")
# Take the input from the user i.e number of days the user want add the given date
days=int(input("days to add the current date: "))
year, month, day = d.split('-')
d = datetime.date(int(year), int(month), int(day)) # converting string data into int 
d = d+timedelta(days)
print(d)
# print weekday using date.weekday() by passing d as argument
print("weekday(0-6):",date.weekday(d))

# print date.isoweekday() by passing d as argument
print("weekday(1-7):",date.isoweekday(d))


