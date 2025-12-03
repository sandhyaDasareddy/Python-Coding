'''
11. Count Factors
-------------

Description
-----------
Write a program to count factors of a given number.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print the integer count.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
20
Output:
6

Sample Case 2
--------------
Input:
15
Output:
4

Constraints
-----------
1 <= n <= 10^6

'''

num = int(input())

count = 0

for i in range(1,num+1):
    if num%i==0:
        count=count+1
print(count)
