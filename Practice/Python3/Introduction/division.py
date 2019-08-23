"""
https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true

Task
Read two integers and print two lines.
The first line should contain integer division, a // b
The second line should contain float division, a / b
You don't need to perform any rounding or formatting operations.
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())

# The first line should contain integer division
print(a // b)

# The second line should contain float division
print(a / b)