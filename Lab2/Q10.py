#Write a Python program to reverse a tuple.
values = input("Input elements with some comma seprated: ")
list = values.split(",")
tuple = tuple(list)
print('Tuple : ',tuple)
a= tuple[::-1]   
print("The reversed tuple is: ",a)  
