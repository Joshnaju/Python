#Write a Python program to remove newline characters from a file.      
def remove_newlines():
    while True:
         file_name = input("Enter file name(test.txt): ")
         try:
          if file_name == "":
           break
          flist = open(file_name).readlines()
          return [s.rstrip('\n') for s in flist]
         except:
          print('File cannot be opened:', file_name)
print(remove_newlines())

