## Problem 4
def largestPalindromeProduct(n):
    upperLimit = 10**(n)
    lowerLimit = upperLimit//10
    palindromes = []

    for i in range(upperLimit, lowerLimit,-1):
        for j in range(i, lowerLimit,-1):
            product = i*j

            if isPalindrome(product):
                palindromes.append(product)
                
    return max(palindromes)

def isPalindrome(n):
    return str(n)==str(n)[::-1]