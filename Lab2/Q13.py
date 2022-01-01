#Write a Python program to generate all sublists of a list.
list1 = []
result_list=[]
total=0
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    list1.append(numbers)
print("Elements in given list is :", list1)
for i in range(len(list1) + 1):
    for j in range(i + 1, len(list1) + 1):
        result_list.append(list1[i:j])
print("Sublists of a list",result_list)

