'''
19. Largest Number of Two
-------------------------

Description
-----------
Write a Java program to find the largest number among two given integers.

Input Format
------------
The first line contains the first integer n. The second line contains the second integer m.

Output Format
-------------
Print the largest number among the two input numbers.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
10
30
Output:
30

Sample Case 2
-------------
Input:
5
5
Output:
5

Constraints
-----------
Both integers are in the range of [-10^9, 10^9].

'''

num1 = int(input())
num2 = int(input())

if num1>num2:
    print(num1)
else:
    print(num2)