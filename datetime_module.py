import datetime

mytime = datetime.time(2, 24, 45, 3000) # Specifies the hour, minutes, seconds, microseconds

print(mytime)
print(mytime.hour)
print(mytime.minute)
print(mytime.second)
print(mytime.microsecond)

today = datetime.date.today() # Inbuilt function to return today's date

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime()) # Returns day of the week, month, date, time, year

from datetime import datetime

mydatetime = datetime(2024, 2, 23, 9, 36, 34)
newdatetime = mydatetime.replace(year=2023)

print(mydatetime)
print(newdatetime)


from datetime import date

date1 = date(2021, 11, 3)
date2 = date(2020, 10, 2)

print(date1 - date2)


datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)

diff = datetime1 - datetime2

print(diff)
print(diff.days)
print(diff.seconds)
print(diff.total_seconds()) # Days (365) converted to seconds + seconds







