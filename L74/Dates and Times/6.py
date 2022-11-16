import datetime
from datetime import date,timedelta
a=((input("date in yyyy-mm-dd format: ")))
year, month, day=a.split('-')
a=datetime.date(int(year), int(month), int(day))
week=int(input("weeks: "))
print("date after",week,"weeks:",a+timedelta(days=7*week))

