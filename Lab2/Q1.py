#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
import itertools
if __name__ == '__main__':
    s='a', 'e', 'i', 'o', 'u'
    p =itertools.permutations(s)
    print([''.join(permutation) for permutation in p])
    
    
