#Write a Python program to count the frequency of words in a file.
with open("test.txt") as f:
    counts = dict()
    for line in f:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    print(counts)
    
 