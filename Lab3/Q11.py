# Write a Python program to get the file size of a plain file
import os
def file_size():
 while True:
  file= input("Enter file name: ") 
  try:  
    if file == "":
         break
    size=os.path.getsize(file)
    print("File Size is :",size, "bytes")
    break
  except:
    print('File cannot be opened:', file)
file_size()
    