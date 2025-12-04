'''
20. Occurrence of Largest Element in an Array
---------------------------------------------

Description
-----------
Write a program to find the occurrence of the largest element in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print the occurrence of largest element

Sample Case 1
-------------
Input:
4
1 2 3 4
Output:
1

Sample Case 2
-------------
Input:
7
1 2 3 4 5 6 7
Output:
1

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6
'''

N = int(input())
arr = list(map(int, input().split()))

largest_number = max(arr)

count = 0

for i in arr:
    if i == largest_number:
        count += 1

print(count)

'''
(OR)

N = int(input())
arr = list(map(int, input().split()))

largest = max(arr)
print(arr.count(largest))


'''