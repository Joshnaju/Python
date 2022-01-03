#Write a Python program to copy the contents of a file to another file.
def file():
 while True:
  file_name = input("Enter file name(test.txt): ")
  try:
   if file == "":
    break
   with open(file_name) as f:
    with open("another.txt", "w") as f1:
        for line in f:
           f1.write(line)
    print("Contents of file", file_name, "is copied to another file successfully")
    break
  except:
       print('File cannot be opened:', file_name)
file()