'''
21. Occurrence of Smallest Element in an Array
-----------------------------------------------

Description
-----------
Write a program to find the occurrence of the smallest element in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print the occurrence of smallest element

Sample Case 1
-------------
Input:
4
1 2 3 1
Output:
2

Sample Case 2
-------------
Input:
7
1 2 3 4 5 6 1
Output:
2

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6
'''
N = int(input())
arr = list(map(int, input().split()))

smallest_element = min(arr)

count = 0

for i in arr:
    if i == smallest_element:
        count += 1

print(count)

'''
(OR)

N = int(input())
arr = list(map(int, input().split()))

smallest = min(arr)
print(arr.count(smallest))

'''