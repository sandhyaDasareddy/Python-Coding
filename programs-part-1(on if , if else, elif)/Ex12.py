'''
12. Equivalent ASCII Character
------------------------------

Description
-----------
Print the equivalent ASCII character of a given number.

Input Format
------------
The input consists of a single integer 'n'.

Output Format
-------------
Output the equivalent ASCII character.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
98
Output:
b

Sample Case 2
-------------
Input:
72
Output:
H

Constraints
-----------
0 <= n <= 127

'''
num = int(input())

print(chr(num))