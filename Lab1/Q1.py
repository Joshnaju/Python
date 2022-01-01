#Tells the user when they turn 100 years old.
from datetime import date
todays_date = date.today()
name=input("Enter name:")
age=int(input("Enter age:"))
user_age = (100 - age) + todays_date.year
print ("In",user_age ,name,"will turn 100 years old.")