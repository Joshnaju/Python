#Write a Python program to calculate the sum of the positive integers 
# of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_integer(num):    
      if num < 1:
       return 0
      else:
       return num + sum_integer(num - 2)
num=int(input("Enter a integer: "))   
print(sum_integer(num))
