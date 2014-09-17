#!/usr/bin/python

# https://projecteuler.net/problem=\15

n=20
row1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
rowj=row1[:]
for i in range(1,n+1):
    row1=rowj[:]
    for j in range(1,n+1):
        rowj[j]=row1[j]+rowj[j-1]
print rowj[n]
