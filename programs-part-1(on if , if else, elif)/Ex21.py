'''
21. Largest Number of Three
---------------------------

Description
-----------
Find the largest number among three integers.

Input Format
------------
The input consists of three space-separated integers 'n', 'm', and 'l'.

Output Format
-------------
Output the largest number among the three.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
10 25 5
Output:
25

Sample Case 2
-------------
Input:
-3 0 -7
Output:
0

Constraints
-----------
All input integers are within the range of a 32-bit signed integer.

'''
n1,n2,n3 = map(int,input().split())

if n1>n2 and n1>n3:
    print(n1)
elif n2>n3:
    print(n2)
else:
    print(n3)