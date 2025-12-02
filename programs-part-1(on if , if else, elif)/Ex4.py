'''
4. Multiple of 5 and 3
----------------------

Description
-----------
Check whether the given number is a multiple of both 5 and 3.

Input Format
------------
The input consists of a single integer 'n'.

Output Format
-------------
Output 'Yes' if the number is a multiple of both 5 and 3, otherwise output 'No'.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
15
Output:
Yes

Sample Case 2
-------------
Input:
30
Output:
Yes

Constraints
------------
0 <= n <= 10^9

'''
num = int(input())
if num%3==0 and num%5==0:
    print("Yes")
else:
    print("No")