#Write a Python program to find the index of an item of a tuple.
values = input("Input elements with some comma seprated: ")
list = values.split(",")
tuple = tuple(list)
print('Tuple : ',tuple)
find=input("Enter the element whose index to be found ")
x=tuple.index(find)
print("The index of", find ,"is",x)



