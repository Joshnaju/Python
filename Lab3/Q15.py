#Write a Python program to read a random line from a file.
import random
while True:
    file_name = input("Enter file name(test.txt): ")
    try:
        if file_name == "":
            break       
        random_lines = random.choice(open( file_name).readlines())
        print(random_lines)
        break
    except:
        print('File cannot be opened:', file_name)
        