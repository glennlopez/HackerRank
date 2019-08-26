'''
https://www.hackerrank.com/challenges/30-data-types/problem

- Lesson learned:
    - Declaring datatypes in python3 requests you to cast the datatype
        - ie:   (C)         ->      float j = 0.0;
                (python)    ->      j = float(input())
'''

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
# Read and save an integer, double, and String to your variables.
j = int(input())
k = float(input())
l = input()

# Print the sum of both integer variables on a new line.
print(i + j)

# Print the sum of the double variables on a new line.
print(d + k)

# Concatenate and print the String variables on a new line
print(s + l)

# The 's' variable above should be printed first.
