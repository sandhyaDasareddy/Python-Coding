'''
12. Sum Divisible Elements
--------------------------

Description
-----------
Write a program to find the sum of elements which are divisible by 3 and 5 in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print sum of elements which are divisible by 3 and 5 in an array

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
0

Sample Case 2
-------------
Input:
5
15 30 35 40 45
Output:
90

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6

'''
N = int(input())
arr = list(map(int, input().split()))

sum_Of_Elements = 0

for i in arr:
    if i % 15 == 0:      # divisible by 3 and 5
        sum_Of_Elements += i

print(sum_Of_Elements)
