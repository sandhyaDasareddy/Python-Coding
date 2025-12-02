'''
5. Multiple of 5, 3, and 7
--------------------------

Description
-----------
Check whether the given number is a multiple of 5, 3, and 7.

Input Format
------------
The input consists of a single integer 'n'.

Output Format
-------------
Output 'Yes' if the number is a multiple of 5, 3, and 7, otherwise output 'No'.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
14
Output:
No

Sample Case 2
-------------
Input:
105
Output:
Yes

Constraints
-----------
0 <= n <= 10^9

'''
num = int(input())
if num%3==0 and num%5==0 and num%7==0:
    print("Yes")
else:
    print("No")