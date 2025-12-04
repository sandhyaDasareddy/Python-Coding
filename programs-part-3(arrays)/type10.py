'''
10. Odd Elements Sum
--------------------

Description
-----------
Write a program to find the sum of all odd elements present in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print sum of all odd elements in an array.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
4

Sample Case 2
-------------
Input:
6
1 2 3 4 5 6
Output:
9

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6
'''

N = int(input())
arr = list(map(int, input().split()))

odd_Elements_sum = 0

for i in arr:
    if i % 2 != 0:
        odd_Elements_sum += i

print(odd_Elements_sum)

'''
    OR
    
N = int(input())
arr = list(map(int, input().split()))
print(sum(x for x in arr if x % 2 != 0))

'''