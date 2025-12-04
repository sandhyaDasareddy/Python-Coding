'''
8. Array Elements Sum
---------------------

Description
-----------
Write a program to find the sum of all elements present in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print sum of all elements in an array.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
24

Sample Case 2
-------------
Input:
6
1 2 3 4 5 6
Output:
21

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6
'''

'''
N = int(input())

arr = list(map(int,input().split()))

print(sum(arr))


    OR

'''

N = int(input())
arr = list(map(int, input().split()))

sum_of_elements = 0

for i in arr:
    sum_of_elements += i

print(sum_of_elements)
