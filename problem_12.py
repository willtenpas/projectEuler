#!/usr/bin/python

# https://projecteuler.net/problem=\12

import sys

test = 0

for i in range(1,10000):
    test+=i
    print 'testing',test
    factors = 1
    for j in range(2,int(test/2.)):
        if test%j==0: factors+=1
        if factors>500:
            print test
            sys.exit()
