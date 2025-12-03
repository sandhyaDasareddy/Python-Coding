'''
1. First N Numbers
------------------

Description
-----------
Write a program to print the first N natural numbers.

Input Format
------------
First line consists of a positive integer n

Output Format
------------
Print the number from 1 to n space separated integer.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
10
Output:
1 2 3 4 5 6 7 8 9 10

Sample Case 2
-------------
Input:
3
Output:
1 2 3
Constraints
1 <= n <= 10^3

'''
num = int(input())

for i in range(1,num+1):
    print(i,end=" ")