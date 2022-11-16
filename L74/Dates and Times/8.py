import datetime
from datetime import date
d=input("date in yyyy-mm-dd format: ")
year, month, day=d.split('-')
d=datetime.date(int(year), int(month), int(day))
print("date, time object:",d)
print(d.isoweekday(),"day of week")