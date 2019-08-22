#!/bin/python3
#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true


#N = int(input())
N = 20

if N % 2 != 0: # is odd
    print("Weird")
elif N % 2 == 0 and N in range(2,5): # is even 2-5
    print("Not Weird")
elif N % 2 == 0 and N in range(6, 20): # is even 6-20
    print("Weird")
elif N % 2 == 0 and N > 20:
    print("Not Weird")
else:
    print("Weird")