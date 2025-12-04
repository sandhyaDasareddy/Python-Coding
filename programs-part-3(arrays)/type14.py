'''

14. Absolute Sum Array
----------------------

Description
-----------
Write a program to find the absolute sum of all elements present in an array.

Input Format
------------
First line contains a single integer N.
Second line contains N space separated integer values.

Output Format
-------------
Print Absolute sum of all elements in an array.

Sample Test Cases
-----------------

Sample Case 1
--------------
Input:
6
1 -4 -6 3 10 -20
Output:
44

Sample Case 2
-------------
Input:
5
5 -10 -15 20 -25
Output:
75

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6
'''

N = int(input())
arr = list(map(int, input().split()))

sum_of_all = 0

for i in arr:
    if i > 0:
        sum_of_all += i
    else:
        i = -i
        sum_of_all += i

print(sum_of_all)


'''
    OR

N = int(input())
arr = list(map(int, input().split()))

print(sum(abs(x) for x in arr))


(or)

N = int(input())
arr = list(map(int, input().split()))

print(sum(map(abs, arr)))




'''
