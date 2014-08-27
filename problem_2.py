#!/usr/bin/python

# https://projecteuler.net/problem=2

fibo=[1,2]

while True:
    fibo.append(fibo[-1]+fibo[-2])
    if fibo[-1]>4000000:        break

print sum(filter(lambda x:x%2==0,fibo))
