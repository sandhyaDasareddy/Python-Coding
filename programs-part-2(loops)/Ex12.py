'''
12. Prime Check
---------------

Description
-----------
Write a program to find whether the given number is a prime number or not.

Input Format
------------
First line consists of a positive integer n

Output Format
-------------
Print Yes if the number is prime, else print No

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
11
Output:
Yes

Sample Case 2
-------------
Input:
15
Output:
No

Constraints
-----------
1 <= n <= 10^6

'''
num = int(input())

if num <= 1:
    print("No")
else:
    status = True
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            status = False
            break
    if status:
        print("Yes")
    else:
        print("No")