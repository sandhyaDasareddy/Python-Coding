'''
13. Common Factors
------------------

Description
-----------
Write a program to find common factors of given 2 integers.

Input Format
------------
First line contains space separated three integer input n, m.

Output Format
-------------
Print space separated common factors of 2 numbers.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
10 20
Output:
1 2 5 10

Sample Case 2
-------------
Input:
15 30
Output:
1 3 5 15

Constraints
-----------
1 <= n, m <= 10^6

'''

a, b = map(int, input().split())

limit = min(a, b)

for i in range(1, limit + 1):
    if a % i == 0 and b % i == 0:
        print(i,end=" ")
       
