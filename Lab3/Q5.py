#Write a Python program to read a file line by line and store it into a list.
with open("test.txt","r") as f:
    content_list = f.readlines()
content_list = [x.strip() for x in content_list]
print(content_list)

