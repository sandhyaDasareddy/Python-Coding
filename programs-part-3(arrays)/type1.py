'''
Reverse Array Elements
----------------------

Description
-----------
Write a program to print numbers present in each index in an array in reverse order.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print space separated integer values stored in each index in the array in reverse order.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
10 3 6 4 1

Sample Case 2
-------------
Input:
4
20 30 40 50
Output:
50 40 30 20

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6

'''
n = int(input())

arr = list(map(int,input().split()))

for i in range(n-1,-1,-1):
    print(arr[i],end=" ")
