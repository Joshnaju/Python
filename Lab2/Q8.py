#Write a Python program to get the 4th element and 4th element from last of a tuple.
values = input("Input elements with some comma seprated: ")
list = values.split(",") 
tuple = tuple(list) 
if len(tuple)>4:   
 print('Tuple : ',tuple)
 element1= tuple[3]
 print("The 4th element  from start of tuple is",element1)
 element2= tuple[-4]
 print("The 4th element from last of tuple is",element2)
else:
    print("Enter atleast 4 elements") 
 
 
