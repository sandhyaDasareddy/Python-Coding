'''
25. Index of K Value in Array
-----------------------------

Description
-----------
The goal of this task is to write a Java program that finds the index of a given value K in a given array. If K is not found in the array, the program should print -1.

Input Format
------------
The first line contains a single integer, N, representing the size of the array.
The second line contains N space-separated integers, representing the elements of the array.
The third line contains a single integer, K, representing the value to be found.

Output Format
-------------
Print the index of the first occurrence of K in the array. If K is not found, print -1.

Sample Case 1
-------------
Input:
7
5 9 2 8 3 7 2
2
Output:
2

Sample Case 2
-------------
Input:
6
1 4 6 3 10 8
5
Output:
-1

Constraints
-----------
1 ≤ N ≤ 10^5 (the size of the array),
-10^9 ≤ elements of the array ≤ 10^9,
-10^9 ≤ K ≤ 10^9
'''

N = int(input())
arr = list(map(int, input().split()))
k = int(input())

found = False

for i in range(N):
    if arr[i] == k:
        print(i)
        found = True
        break

if not found:
    print(-1)




