'''
14. Uppercase ASCII Check
-------------------------

Description
-----------
Check if a given number is the ASCII value of an uppercase alphabet or not.

Input Format
------------
The input consists of a single line containing an integer, n.

Output Format
--------------
Print 'Yes' if the number is an ASCII value of an uppercase alphabet, and 'No' otherwise.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
78
Output:
Yes
Sample Case 2
-------------
Input:
88
Output:
Yes

Constraints
------------
The input integer is in the range of 65 to 90.

'''

num = int(input())
if num>=65 and num<=90:
    print("Yes")
else:
    print("No")
