'''
16. Multiplication or Addition
--------------------------

Description
-----------
Check the given two integer inputs. If both numbers are even, find their product. Otherwise, find their sum.

Input Format
------------
The input consists of two lines. The first line contains the first integer, n. The second line contains the second integer, m.

Output Format
--------------
Print the product of the two numbers if both numbers are even. Otherwise, print their sum.

Sample Test Cases
-----------------

Sample Case 1
-------------
Input:
10
20
Output:
200

Sample Case 2
-------------
Input:
10
15
Output:
25

Constraints
-----------
The input integers are in the range of -10^9 to 10^9.

'''
first_num = int(input())
second_num = int(input())

if first_num%2==0 and second_num%2==0:
    print(first_num*second_num)
else:
    print(first_num+second_num)