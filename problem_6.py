#!/usr/bin/python

# https://projecteuler.net/problem=6

target = 100

sumOFsquare = 0
squareOFsum = 0

for i in range(1,target+1):
    sumOFsquare+=i**2
    squareOFsum+=i

print squareOFsum**2-sumOFsquare
