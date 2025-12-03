'''
14.Highest Common Factor
------------------------

Description
-----------
Write a program to find the greatest common factor of given 2 integers.

Input Format
------------
First line contains space separated three integer input n, m.

Output Format
-------------
Print greatest common factor of 2 numbers.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
10 20
Output:
10

Sample Case 2
-------------
Input:
15 30
Output:
15

Constraints
-----------
1 <= n, m <= 10^6

'''
a,b = map(int,input().split())

limit = min(a,b)

for i in range(limit,0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break

'''

import math
a, b = map(int, input().split())
print(math.gcd(a, b))

'''