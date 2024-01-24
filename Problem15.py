## Problem 15
import math

def lattice_paths(gridSize):
    factorial_2n = math.factorial(2 * gridSize)
    factorial_n = math.factorial(gridSize)
    return factorial_2n // (factorial_n * factorial_n)
