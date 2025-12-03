'''
6. Multiples of Two
-------------------

Description
-----------
Write a program to print all the multiples of 2 till N.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print the numbers from 2 to n which are multiples of 2.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
15
Output:
2 4 6 8 10 12 14

Sample Case 2
-------------
Input:
3
Output:
2

Constraints
-----------
2 <= n <= 10^3

'''

num = int(input())

for i in range(2,num+1,2):
    print(i,end=" ")