# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
from random import randrange
target = randrange(1, 10)
guess_num = int(input("Guess a number between 1 and 9 :"))
while (guess_num >= 10) or (guess_num<=0):
    guess_num = int(input("Entered number is above 9 or below 1. please, Guess a number between 1 and 9 :"))
else:
    print("Random number is", target)
if target > guess_num:
    print("The guessed number is too low")
elif target < guess_num:
    print("The guessed number is too high")
else:
    print("Gussed the exact number")
