'''
22. Second Largest Number
-------------------------

Description
-----------
Find the second largest number in a given array of integers. Where second largest number must be different from first largest number.

Input Format
------------
The first line contains a single integer, N, representing the size of the array.
The second line contains N space-separated integers, representing the elements of the array.

Output Format
-------------
Print the second largest number in the array.

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
6

Sample Case 2
-------------
Input:
8
3 8 2 10 5 9 7 1
Output:
9

Constraints
------------
2 ≤ N ≤ 10^5 (the size of the array) -10^9 ≤ elements of the array ≤ 10^9
'''

N = int(input())
arr = list(map(int, input().split()))

unique_arr = list(set(arr))
unique_arr.sort()

print(unique_arr[-2])

