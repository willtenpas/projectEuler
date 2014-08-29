#!/usr/bin/python

# https://projecteuler.net/problem=4


# sol 1
def isPalindrome(x):
    if str(x)==str(x)[::-1]: return True
    else: return False
biggest = 0
for x in range(100,999):
    for y in range(x,999):
        if isPalindrome(x*y) and x*y > biggest: biggest = x*y
print biggest


#sol 2
print max(a*b for a in range(100,1000) for b in range(a,1000) if str(a*b) == str(a*b)[::-1])
