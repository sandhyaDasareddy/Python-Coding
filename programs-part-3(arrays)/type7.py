'''
7. Reverse Odd Array
--------------------

Description
----------
Write a program to print odd numbers present in an array in reverse order.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print space separated odd integer values stored in an array in reverse order.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
3 1

Sample Case 2
-------------
Input:
6
2 3 4 5 6 7
Output:
7 5 3

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6

'''
N = int(input())

arr = list(map(int,input().split()))

for i in range(N-1,-1,-1):
    if(arr[i]%2!=0):
        print(arr[i],end=" ")