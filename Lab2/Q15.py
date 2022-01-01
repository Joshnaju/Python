#Write a password generator in Python.
import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()`~}{][_+-=\|:;'<>?/.,")
def generate_password():
	password_len= int(input("Enter password length: "))
	random.shuffle(characters)
	password = []
	for i in range(password_len):
		password.append(random.choice(characters))
	random.shuffle(password)
	print("".join(password))
generate_password()
