'''
11. Divisible Elements Print
----------------------------

Description
-----------
Write a program to print the elements which are divisible by 2 and 3 in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print elements which are divisible by 2 and 3 in an array

Sample Test Cases
-----------------

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
5
2 3 6 9 12
Output:
6 12

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6

'''

N = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if i%6==0:
        print(i,end=" ")


'''

    OR
    
N = int(input())

arr = list(map(int,input().split()))

print(*[x for x in arr if x % 6 == 0])
'''
