'''
9. Three Digit Number and Multiple of 2, 5, and 10
--------------------------------------------------

Description
-----------
Check if a given number is a three-digit number and also a multiple of 2, 5, and 10.

Input Format
------------
The input consists of a single integer 'n' on a single line.

Output Format
-------------
Output 'Yes' if the number is a three-digit number and a multiple of 2, 5, and 10, otherwise output 'No'.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
140
Output:
Yes

Sample Case 2
-------------
Input:
145
Output:
No

Constraints
-----------
0 <= n <= 10^9

'''
num = int(input())

if (num>99 and num<1000) and (num%2==0 and num%5==0 and num%10==0):
    print("Yes")
else:
    print("No")