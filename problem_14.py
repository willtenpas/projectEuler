#!/usr/bin/python

# https://projecteuler.net/problem=\14

longest=1

for i in range(1000000,1,-1):
    num=i
    sequence=[]
    while num != 1:
        sequence.append(num)
        if num%2==0: num/=2
        else: num=num*3+1
    if len(sequence)>longest:
        print i,len(sequence)
        longest=len(sequence)
