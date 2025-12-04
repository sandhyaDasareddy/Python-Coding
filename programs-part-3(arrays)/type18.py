'''
18. Smallest Element in an Array
--------------------------------

Description
-----------
Given an array of integers of size N, find and display the smallest element present in the array.

Input Format
------------
The first line contains an integer N, the size of the array.
The second line contains N space-separated integers representing the array elements.

Output Format
-------------
Print the smallest element present in the array.

Sample Case 1
-------------
Input:
5
1 5 7 3 2
Output:
1

Sample Case 2
-------------
Input:
6
0 -1 -2 -3 -4 -5
Output:
-5

'''

N = int(input())
arr = list(map(int, input().split()))

smallest = arr[0]

for i in range(1, N):
    if arr[i] < smallest:
        smallest = arr[i]

print(smallest)

'''
(OR)

N = int(input())
arr = list(map(int, input().split()))

print(min(arr))

'''