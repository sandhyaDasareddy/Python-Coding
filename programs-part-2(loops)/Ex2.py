'''
2. First N Evens
----------------

Description
-----------
Write a program to print the first N even natural numbers.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print the number from 1 to n space separated even integer.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
Output:
2 4 6 8 10

Sample Case 2
-------------
Input:
3
Output:
2 4 6

Constraints
-----------
1 <= n <= 10^3

'''
n = int(input())

for i in range(1, n + 1):
    print(i * 2, end=" ")
