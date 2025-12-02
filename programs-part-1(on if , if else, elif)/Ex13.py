'''
13. Lowercase ASCII Value
-------------------------

Description
-----------
Check if a given number is the ASCII value of a lowercase alphabet.

Input Format
------------
The input consists of a single integer 'n'.

Output Format
-------------
Output 'Yes' if the number is the ASCII value of a lowercase alphabet, otherwise output 'No'.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
100
Output:
Yes

Sample Case 2
-------------
Input:
108
Output:
Yes

Constraints
-----------
97 <= n <= 122

'''
num = int(input())

if num>=97 and num<=122:
    print("Yes")
else:
    print("No")