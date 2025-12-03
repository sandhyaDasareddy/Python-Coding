'''
3. First N Odds
---------------

Description
-----------
Write a program to print the first N odd natural numbers.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print the number from 1 to n space separated odd integers.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
Output:
1 3 5 7 9

Sample Case 2
-------------
Input:
3
Output:
1 3 5

Constraints
-----------
1 <= n <= 10^3

'''

num = int(input())

for n in range(1,num+1):
    print(n*2-1,end = " ")