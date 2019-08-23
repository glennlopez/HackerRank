"""
https://www.hackerrank.com/challenges/python-loops/problem

Task
Read an integer n.
For all non-negative integers i < n, print i^2. See the sample for details.
"""

if __name__ == '__main__':
    n = int(input())


for i in range(0, n):
    print(i ** 2)



"""
Needed to learn to solve:
    - ranged for loops
    - exponent syntax in python: 1 ** 2
"""