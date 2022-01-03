#Write a Python program to calculate the sum of a list of numbers
list=[]
sum=0
n=int(input("Enter number of elements in the list: "))    
while True:  
  try:  
   for x in range(n):
    element=int(input("Enter integer element: "))  
    list.append(element)
   print("The list is ",list)
   for e in list:
     sum=sum+e
   print("Sum of elements in list is ",sum) 
   break 
  except:
      print("Enter only integers")
 
