#Write a Python program to write a list to a file.
list=[]
n=int(input("Enter how many elements in list "))
for x in range(n):
    element=input("Enter element: ")
    list.append(element)
print("The list is",list)
file= input("Enter file name(test1.txt): ") 
with open(file, 'w+') as f:
    for items in list:
        f.write('%s\n' % items)
print("File written successfully")


   