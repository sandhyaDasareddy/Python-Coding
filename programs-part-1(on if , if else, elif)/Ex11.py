'''
11.ASCII Value of Character
---------------------------

Description
-----------
Print the ASCII value of a character.

Input Format
------------
The input consists of a single character 'c' on a single line.

Output Format
-------------
Output the ASCII value of the character as an integer.

Sample Test Cases
----------------

Sample Case 1
-------------
Input:
A
Output:
65

Sample Case 2
-------------
Input:
a
Output:
97

Constraints
-----------
The character 'c' is a valid ASCII character.

'''
char = input().strip()

print(ord(char))