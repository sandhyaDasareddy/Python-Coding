'''
7. Multiples of Two & Three
--------------------------

Description
-----------
Write a program to print all the numbers which are multiples of either 2 or 3 till N.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print the number from 2 to n space separated multiples of 2 and 3 integers.

Sample Test Cases
------------------

Sample Case 1
-------------
Input:
15
Output:
2 3 4 6 8 9 10 12 14 15

Sample Case 2
-------------
Input:
10
Output:
2 3 4 6 8 9 10

Constraints
-----------
2 <= n <= 10^3

'''

num = int(input())

for i in range(2,num+1):
    if i%2==0 or i%3==0:
        print(i,end=" ")