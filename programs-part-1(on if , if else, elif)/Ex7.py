'''
7. Three Digit Number
---------------------

Description
-----------
Check whether the given number is a three-digit number or not.

Input Format
------------
The input consists of a single integer 'n'.

Output Format
-------------
Output 'Yes' if the number is a three-digit number, otherwise output 'No'.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
145
Output:
Yes

Sample Case 2
-------------
Input:
1000
Output:
No

Constraints
-----------
0 <= n <= 10^9
'''
num = int(input())

if num>99 and num<1000:
    print("Yes")
else:
    print("No")