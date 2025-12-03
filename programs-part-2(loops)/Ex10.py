'''
10. Factors
-----------

Description
-----------
Write a program to find factors of a given number.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print the space separated integer factors of given number.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
20
Output:
1 2 4 5 10 20

Sample Case 2
-------------
Input:
15
Output:
1 3 5 15

Constraints
-----------
1 <= n <= 10^6

'''

num = int(input())

for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")
