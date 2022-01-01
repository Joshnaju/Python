#Write a Python program to get the key, value and item in a dictionary.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("The key:")
for x in dict_num:
    print(x)
print("The value:")    
for x in dict_num.values():
    print(x)   
print("The key and value(item):") 
for x,y in dict_num.items():
    print(x,y)
        