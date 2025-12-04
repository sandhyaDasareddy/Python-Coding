'''
15. Average of Array
---------------------

Description
-----------
Write a program to find the average of all elements present in an array.

Input Format
------------
First line contains a single integer N. Next line contains N space separated integer values.

Output Format
-------------
Print float value of average of all elements in an array. [it has to print 2 decimal points]

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
5
1 4 6 3 10
Output:
4.80

Sample Case 2
-------------
Input:
5
5 -10 -15 20 -25
Output:
-5.00

Constraints
-----------
1 <= N <= 10^3 -10^6 <= array elements <= 10^6

'''

N = int(input())
arr = list(map(int, input().split()))

sum_of_all = 0

for i in arr:
    sum_of_all += i

average_of_elements = sum_of_all / N

print(f"{average_of_elements:.2f}")


'''
    OR

N = int(input())
arr = list(map(int, input().split()))

average = sum(arr) / N
print(f"{average:.2f}")

'''
