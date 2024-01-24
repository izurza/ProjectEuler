## Problem 14 
def longest_collatz_sequence(n):
    max_chain_number = 0
    max_chain = 0
    for x in range(n+1):
        current = x
        current_chain=0
        while(current>1):
            current = even_op(current) if is_even(current) else odd_op(current)
            current_chain+=1
        max_chain_number, max_chain = (x, current_chain) if current_chain > max_chain else (max_chain_number, max_chain)
    return max_chain_number

def even_op(n):
    return n/2

def odd_op(n):
    return 3*n+1

def is_even(n):
    return n%2==0