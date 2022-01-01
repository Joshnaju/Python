#Ask the user for a string and print out whether this string is a palindrome or not
s=input("Enter a string:")
str1 = ""
for i in s:
    str1 = i + str1  
print("String in reverse Order :  ", str1)
if(s== str1):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")