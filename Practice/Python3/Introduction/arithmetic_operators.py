'''
https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

Task
Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''


if __name__ == '__main__':
    a = int(input())
    b = int(input())

# The first line contains the sum of the two numbers.
print(a + b)

# The second line contains the difference of the two numbers (first - second).
print(a - b)

# The third line contains the product of the two numbers.
print(a * b)