'''
8. Multiples of TwoFiveSeven
----------------------------

Description
-----------
Write a program to print all the numbers which are multiples of either 2, 5 or 7 till N.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print the number from 2 to n space separated multiples of 2, 5 and 7 integers.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
15
Output:
2 4 5 6 7 8 10 12 14 15

Sample Case 2
-------------
Input:
10
Output:
2 4 5 6 7 8 10

Constraints
-----------
2 <= n <= 10^3

'''

num = int(input())

for i in range(2,num+1):
    if i%2==0 or i%5==0 or i%7==0:
        print(i,end=" ")