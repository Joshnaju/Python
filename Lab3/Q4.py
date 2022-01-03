#Write a Python program to read last n lines of a file. 
def read_lastnlines(n):
    with open('test.txt') as f:
	    for line in (f.readlines() [-n:]):
		    print(line)
n=int(input("last n lines: "))
read_lastnlines(n)