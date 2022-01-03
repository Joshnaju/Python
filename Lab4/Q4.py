#Write a Python program to get week number from 16/06/2015

import datetime
print(datetime.date(2015, 6, 16).isocalendar()[1])

#datetime.date.isocalendar() is an instance-method returning a tuple 
# containing year, weeknumber and weekday in respective order for the 
# given date instance.

