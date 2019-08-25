"""
https://www.hackerrank.com/challenges/list-comprehensions/tutorial

list_name = [expr for val in collection]
list_name = [expr for val in collection if <test>]
list_name = [expr for val in collection if <test> and <test2>]
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# debug
print(x, y, z, n, sep=",")

#squares = [i**2 for i in range(1, 101)]
#print(squares, sep=' ')

lexicon = [[]]
print(lexicon)


"""
Need to learn:
    - list comprehension:
        https://www.youtube.com/watch?v=AhSvKGTh28Q
"""