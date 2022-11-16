import datetime
from datetime import date
from datetime import timedelta

# take the date input from the user
d=input('date in yyyy-mm-dd format: ')
year, month, day = d.split('-')
d = datetime.date(int(year), int(month), int(day))
print('adding 3 days:',d+timedelta(days=3))
# add 3 days to the given date using timedelta function

# print the new date