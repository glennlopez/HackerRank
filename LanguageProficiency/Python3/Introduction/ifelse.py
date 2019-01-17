#!/bin/python3

'''
https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
Given an integer, n , perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
'''

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