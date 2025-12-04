'''
23. Second Smallest Number

Description
-----------
Write a program that finds the second smallest number in a given array of integers.

Input Format
------------
The first line contains a single integer, N, representing the size of the array. The second line contains N space-separated integers, representing the elements of the array.

Output Format
-------------
Print the second smallest number in the array.

Sample Case 1
-------------
Input:
6
5 9 2 8 3 7
Output:
3

Sample Case 2
-------------
Input:
7
10 5 8 2 6 1 4
Output:
2

Constraints
-----------
- 2 ≤ N ≤ 10^5 (the size of the array)
-10^9 ≤ elements of the array ≤ 10^9
'''

N = int(input())

arr = list(map(int, input().split()))

unique_arr = list(set(arr))
unique_arr.sort()

print(unique_arr[1])
