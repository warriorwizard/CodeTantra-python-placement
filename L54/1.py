from datetime import datetime
dob=(input("dob in ddmmyyyy format: "))
tod=(input("today's date in ddmmyyyy format: "))
a=datetime.strptime(dob,'%d%m%Y')
b=datetime.strptime(tod, '%d%m%Y')
k=b-a
print("days since birthday:",k.days)