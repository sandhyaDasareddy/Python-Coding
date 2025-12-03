'''Common Multiples
Description
Write a program to print common multiples of 2 numbers.

Input Format
First line contains a single integer input n. Second line contains space separated 2 integer input a, b.

Output Format
Print first n common multiples of a and b.

Sample Test Cases
Sample Case 1
Input:
9
3 4
Output:
12 24 36 48 60 72 84 96 108
Sample Case 2
Input:
5
5 7
Output:
35 70 105 140 175
Constraints
1 <= n <= 10^3 1 <= a, b <= 10^3

'''

n = int(input())
a, b = map(int, input().split())

count = 0
i = 1

while count < n:
    if i % a == 0 and i % b == 0:
        print(i, end=" ")
        count += 1
    i += 1
