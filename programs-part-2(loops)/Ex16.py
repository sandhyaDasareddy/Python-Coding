'''
16. LCF Excluding 1,2
---------------------

Description
-----------
Write a program to find the lowest common factor of given 2 integers excluding 1 and 2.

Input Format
------------
First line contains space separated two integer input n, m.

Output Format
-------------
Print lowest common factor of 2 numbers excluding 1 and 2.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
10 20
Output:
5

Sample Case 2
-------------
Input:
15 30
Output:
3

Constraints
-----------
1 <= n, m <= 10^6

'''

a, b = map(int, input().split())

limit = min(a, b)

for i in range(3, limit + 1):
    if a % i == 0 and b % i == 0:
        print(i)
        break
