#!/usr/bin/python

# https://projecteuler.net/problem=3

import primes

target = 13195
target = 600851475143


factor = 2

while target>1:
    if target%factor==0:
        target/=factor
    else:
        factor = primes.nextPrime(factor)

print factor
