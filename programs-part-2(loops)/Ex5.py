'''
5. Multiples of 5
-----------------

Description
-----------
Write a program to print first N multiples of 5.

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
5
Output:
5 10 15 20 25

Sample Case 2
-------------
Input:
3
Output:
5 10 15

Constraints
-----------
1 <= n <= 10^3

'''
num = int(input())
for i in range(1,num+1):
    print(5*i,end=" ")
