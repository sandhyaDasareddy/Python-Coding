'''
4. Even Numbers Array
---------------------

Description
-----------
Write a program to print even numbers present in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print space separated even integer values in an array.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
4 6 10

Sample Case 2
-------------
Input:
4
20 30 40 50
Output:
20 30 40 50

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6

'''

N = int(input())

arr = list(map(int,input().split()))

for i in range(0,N):
    if arr[i]%2==0:
        print(arr[i],end=" ")