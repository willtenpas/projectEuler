#!/usr/bin/python

# https://projecteuler.net/problem=7

import primes
target = 10001

val=2
for i in range(1,target):
    val = primes.nextPrime(val)

print val
