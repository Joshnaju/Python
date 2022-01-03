#Write a Python program to read first n lines of a file.
with open("test.txt","r") as f:
    n= int(input('How many lines to be displayed: '))
    for i in range(n):
        line =f.readline()
        print(line)