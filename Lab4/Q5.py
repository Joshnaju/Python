#Write a Python program to get days between two dates. Go to the editor 
#Exampe: days between 28/02/2000 and  28/02/2001
from datetime import datetime
for x in range(1,3):
 my_string = str(input('Enter date(yyyy-mm-dd): '))
 my_date = datetime.strptime(my_string, "%Y-%m-%d")
 if x==1:
      date1=my_date.date()
      print("Date1",date1)
 elif x==2:
     date2=my_date.date()
     print("Date2",date2)
 else:
     pass
result=date2-date1
print(result.days,"days")
    
      