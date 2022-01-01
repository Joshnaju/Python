# Write a Python program to sum all the items in a list.
list1 = []
total=0
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    list1.append(numbers)
for x in range(0, len(list1)):
    total = total + list1[x]    
print("Sum of elements in given list is :", total)