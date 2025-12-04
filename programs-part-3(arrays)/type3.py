'''
3. Odd Index Elements
---------------------

Description
-----------
Write a program to print numbers present in the odd index of an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print space separated integer values stored in the odd index of the array.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
4 3

Sample Case 2
-------------
Input:
4
20 30 40 50
Output:
30 50

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6

'''

n = int(input())

arr = list(map(int,input().split()))

for i in range(1,n,2):
    print(arr[i],end=" ")
