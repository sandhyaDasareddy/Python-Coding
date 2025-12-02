'''
17. Positive or Negative Number
-------------------------------

Description
-----------
Check if a given number is greater than 0, if yes then print 'Positive'. If the given number is lesser than 0, then print 'Negative'. If the given number is exactly equal to 0, then print 'Zero'.

Input Format
------------
The input consists of a single integer, n.

Output Format
-------------
Print 'Positive' if n > 0. Print 'Negative' if n < 0. Print 'Zero' if n = 0.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
30
Output:
Positive

Sample Case 2
-------------
Input:
-25
Output:
Negative

Constraints
------------
The input integer is in the range of -10^9 to 10^9.

'''
num = int(input())

if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

