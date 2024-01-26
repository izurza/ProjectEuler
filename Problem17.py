## Problem 17
from num2words import num2words
def number_letter_counts(n):
    res=0
    for x in range(1, n+1):
        res += len(str(num2words(x)).replace(' ','').replace('-',''))
        print(res) 

number_letter_counts(1000)