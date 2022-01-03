#Write a Python program to append text to a file and display the text.
with open("test.txt","a") as f:
    f.write("\nAppending some content to test.txt file")
with open("test.txt", "r") as f:
    print(f.read())
    