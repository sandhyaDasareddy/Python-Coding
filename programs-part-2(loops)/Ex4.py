'''
4. Multiples of 3
-----------------

Description
-----------
Write a program to print first N multiples of 3.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print the required space separated number series

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
7
Output:
3 6 9 12 15 18 21

Sample Case 2
-------------
Input:
3
Output:
3 6 9

Constraints
-----------
1 <= n <= 10^3

'''

num = int(input())

for i in range(1,num+1):
    print(3*i,end=" ")