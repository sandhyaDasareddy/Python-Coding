'''
17. Largest Element in an Array
--------------------------------

Description
-----------
Write a program to find the largest element in a given array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print largest element in an array

Sample Test Cases
-----------------

Sample Case 1
--------------
Input:
5
1 5 7 3 2
Output:
7

Sample Case 2
-------------
Input:
6
0 -1 -2 -3 -4 -5
Output:
0

Constraints
------------
1 <= N <= 10^3 - 10^6 <= array elements <= 10^6
'''
N = int(input())
arr = list(map(int, input().split()))

lar = arr[0]

for i in range(1,N):
    if arr[i] > lar:
        lar = arr[i]

print(lar)

'''
(OR)

N = int(input())
arr = list(map(int, input().split()))
print(max(arr))

'''