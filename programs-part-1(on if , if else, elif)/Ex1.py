'''
1. Even or Odd
--------------

Description
-----------
Check if a given number is even number or odd number

Input Format
------------
First line contains single integer n

Output Format
-------------
Print Yes if it is even number, else No

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
12
Output:
Yes

Sample Case 2
-------------
Input:
15
Output:
No

Constraints
-----------
1 <= n <= 10^6

'''

num = int(input())
if num%2==0:
    print("Yes")
else:
    print("No")