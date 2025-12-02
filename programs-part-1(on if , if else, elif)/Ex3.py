'''
Multiple of 10
--------------
Description
------------
Determine whether the given number is a multiple of 10 or not.

Input Format
------------
The input consists of a single integer 'n'.

Output Format
-------------
Output 'Yes' if the number is a multiple of 10, otherwise output 'No'.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
50
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
if num%10==0:
    print("Yes")
else:
    print("No")