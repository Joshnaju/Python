""" Write a Python script to display the
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
 """
from datetime import datetime,date
print("Current date and time: " ,datetime.now())
print("Current year: ", date.today().strftime("%Y"))
print("Month of year: ", date.today().strftime("%B"))
print("Week number of the year: ", date.today().strftime("%W"))
print("Weekday of the week: ",date.today().strftime("%w"))
print("Day of year: ", date.today().strftime("%j"))
print("Day of the month : ", date.today().strftime("%d"))
print("Day of week: ", date.today().strftime("%A"))


