#Write a Python program to combine each line from first file with the corresponding line in second file.
with open('file1.txt') as f1,open('file2.txt') as f2:
	for l1,l2 in zip(f1,f2):
		l1=l1.strip()
		l2=l2.strip()
		print(l1+l2)
