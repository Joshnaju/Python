#Write a Python program to convert unix timestamp string to readable date
from datetime import date
while True:  
    time_stamp=int(input("Enter the timestamp:"))
    try:
        t=date.fromtimestamp(time_stamp)
        print("The readable date of unix timestamp",time_stamp,"is ",t)
        break
    except:
        print("Enter another timestamp")    