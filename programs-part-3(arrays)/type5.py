'''
5. Odd Numbers Array
--------------------

Description
-----------
Write a program to print odd numbers present in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print space separated odd integer values stored in an array.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
1 3

Sample Case 2
-------------
Input:
4
21 31 41 51
Output:
21 31 41 51

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6

'''
N = int(input())

arr = list(map(int,input().split()))

for i in range(0,N):
    if arr[i]%2!=0:
        print(arr[i],end=" ")