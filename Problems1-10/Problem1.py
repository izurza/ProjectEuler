## Problem 1
def multiplesOf3Or5(number):
  res=0
  for n in range(1,number):
    if (n%3==0 or n%5==0):
        res+=n
  return res
