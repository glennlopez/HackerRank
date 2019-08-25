"""
https://www.hackerrank.com/challenges/python-print/problem

Read an integer N.
Without using any string methods, try to print the following:

    1 2 3 ... N

Note that "" represents the values in between.
"""

if __name__ == '__main__':
    n = int(input())

# most code efficient method
print(*range(1, n + 1), sep='')



"""
Needed to learn:
    - Unpacking operator:
        - *expression: 
            https://www.hackerrank.com/challenges/python-print/forum/comments/180891
        
    - Sep Parameter in Print():
        https://www.geeksforgeeks.org/python-sep-parameter-print/    
"""