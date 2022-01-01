#Write a Python program to remove an item from a set if it is present in the set.
set1=set()
num = int(input("How many numbers: "))
for n in range(num):
    numbers = int(input("Enter number "))
    set1.add(numbers)
print("Elements in given list is :", set1)
remove1 =int(input("\n Enter the element you want to remove :"))
if remove1 in set1:
    set1.remove(remove1)
    print("The updated set :", set1)
else:
    print("\nPlease check, entered element not found\n")
    print("The original set is",set1)
