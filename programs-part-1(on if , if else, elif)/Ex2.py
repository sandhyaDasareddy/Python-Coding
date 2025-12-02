'''
2. Multiple of Five
-------------------

Description
-----------
Determine whether the given number is multiple of 5 or not

Input Format
------------
First line contains single integer n

Output Format
-------------
Print Yes if it is multiple of 5, else No

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
24
Output:
No

Sample Case 2
-------------
Input:
30
Output:
Yes

Constraints
-----------
1 <= n <= 10^6

'''
num = int(input())
if num%5==0:
    print("Yes")
else:
    print("No")