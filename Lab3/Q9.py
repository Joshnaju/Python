#Write a Python program to count the number of lines in a text file.
file= input("Enter file name: ")
try:
    num_lines = 0
    with open(file, 'r') as f:
     for line in f:
          num_lines += 1
    print("Number of lines:",num_lines)
except:
    print('File cannot be opened:', file)
