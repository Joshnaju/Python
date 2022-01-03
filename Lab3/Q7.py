#Write a Python program to read a file line by line store it into an array.
def file_read(file):
    array = []
    with open(file) as f:
        for line in f:
            array.append(line)
        print(array)
file_read('test.txt')