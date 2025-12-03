'''
9. Multiples of ThreeFiveSeven
-------------------------------

Description
-----------
Write a program to print the first N multiples of either 3, 5 or 7.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print the first N multiples of either 3, 5 or 7, space separated.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
10
Output:
3 5 6 7 9 10 12 14 15 18

Sample Case 2
-------------
Input:
5
Output:
3 5 6 7 9

Constraints
-----------
1 <= n <= 10^3

'''

num = int(input())

count = 0
i=1

while(count<num):
    if i%3==0 or i%5==0 or i%7==0:
        print(i,end=" ")
        count += 1
    i += 1
