#!/usr/bin/python

# https://projecteuler.net/problem=5

'''
def test(largest_divisor,x):
    for i in range(largest_divisor/2+1,largest_divisor):
        if x%i!=0: return False
    return True

# brute -- 16 = 720720 then it gets nasty
largest_divisor=5
num=largest_divisor
while True:
    print num
    if test(largest_divisor,num):   break
    else: num+=largest_divisor
'''

largest_divisor = 20
test=largest_divisor
for i in range(largest_divisor,1,-1):
    inc = test
    while test%i!=0:
        test+=inc
print test  
    
