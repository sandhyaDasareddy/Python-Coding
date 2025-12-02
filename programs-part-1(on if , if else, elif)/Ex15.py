'''
15. Number ASCII Check
----------------------

Description
-----------
Check if a given number is the ASCII value of a numeric character or not.

Input Format
------------
The input consists of a single line containing an integer, n.

Output Format
-------------
Print 'Yes' if the number is an ASCII value of a numeric character, and 'No' otherwise.

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
88
Output:
No

Constraints
-----------
The input integer is in the range.

'''
num = int(input())

if num>=48 and num<=57:
    print("Yes")
else:
    print("No")

