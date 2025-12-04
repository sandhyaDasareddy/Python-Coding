'''
16. Even, Odd and Negative Elements in Array
--------------------------------------------

Description
-----------
Write a program to print negative elements, even elements and odd elements present in an array separately.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
First line prints space separated negative elements in an array.
Second line prints space separated odd elements in an array.
Third line prints space separated even elements in an array.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
6
1 -4 -6 3 10 -20
Output:
-4 -6 -20
1 3
10

Sample Case 2
-------------
Input:
5
5 -10 -15 20 -25
Output:
-10 -15 -25
5
20

Constraints
------------
1 <= N <= 10^3 - 10^6 <= array elements <= 10^6

'''

N = int(input())

arr = list(map(int,input().split()))

negative_list=[]
odd_list=[]
even_list=[]

for i in arr:
    if i<0:
        negative_list.append(i)
    elif i%2!=0:
        odd_list.append(i)
    else:
        even_list.append(i)
for i in negative_list:
    print(i,end=" ")

print()

for i in odd_list:
    print(i,end=" ")
    
print()

for i in even_list:
    print(i,end=" ")

