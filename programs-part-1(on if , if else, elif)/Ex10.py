'''
10.Number Ends with Zero
------------------------

Description
-----------
Check if a given number ends with zero or not.

Input Format
------------
The input consists of a single integer 'n' on a single line.

Output Format
-------------
Output 'Yes' if the number ends with zero, otherwise output 'No'.

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

last_digit = num%10

if last_digit==0:
    print("Yes")
else:
    print("No")