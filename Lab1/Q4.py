#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
num=int(input("Enter a number:"))
print("The divisors of the number are:")
divisor= [i for i in range(1,num+1) if num%i==0 ]
print(divisor)
