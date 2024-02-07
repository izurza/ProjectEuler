## Problem 24
from itertools import permutations
def lexicographic_permutations(n):
    return list(permutations([0,1,2,3,4,5,6,7,8,9]))[n]

print(lexicographic_permutations(899999))