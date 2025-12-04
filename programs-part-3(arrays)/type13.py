'''
13. Sum Positive Negative
-------------------------

Description
-----------
Write a program to find the sum of positive elements and negative elements separately in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
First line print sum of positive elements in an array. Second line print sum of negative elements in an array.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
6
1 -4 -6 3 10 -20
Output:
14
-30

Sample Case 2
-------------
Input:
5
5 -10 -15 20 25
Output:
50
-25

Constraints
-----------
1 <= N <= 10^3 - 10^6 <= array elements <= 10^6

'''

N = int(input())
arr = list(map(int, input().split()))

sum_positive_elements = 0
sum_negative_elements = 0

for i in arr:
    if i > 0:
        sum_positive_elements += i
    else:
        sum_negative_elements += i

print(sum_positive_elements)
print(sum_negative_elements)
