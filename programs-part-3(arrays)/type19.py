'''
19. Replace Even Elements in an Array
-------------------------------------

Description
-----------
Write a program to find the even elements in an array and replace all even elements with ‘0’.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print the required output

Sample Case 1
-------------
Input:
5
1 2 3 4 5
Output:
1 0 3 0 5

Sample Case 2
-------------
Input:
6
6 7 8 9 10 11
Output:
0 7 0 9 0 11

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6
'''

N = int(input())

arr = list(map(int,input().split()))

for i in range(0,N):
    if arr[i]%2==0:
        arr[i] = 0

for i in arr:
    print(i,end=" ")

'''

(OR)

N = int(input())
arr = list(map(int, input().split()))

arr = [0 if x % 2 == 0 else x for x in arr]
print(*arr)

'''