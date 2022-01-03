#Write a python program to find the longest words.
n=int(input("Enter the value of n "))
with open("test.txt","r") as f:
    s=f.read()
    l=s.split()
    for i in l:
        if (len(i)>n):
            print(i)
    
