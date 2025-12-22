'''
Program Name:
-------------
Insert an element into a sorted list

Question:
---------
Write a Python program to insert a given number into a sorted list
such that the list remains sorted after insertion.

Input Format:
-------------
1. The first line contains a sorted list of integers entered in list format.
2. The second line contains an integer to be inserted into the list.

Output Format:
--------------
Print the updated list after inserting the given number at the correct position.

Sample Input 1:
---------------
Enter a sorted list between:[]
[10, 20, 30, 40]
Enter number:
25

Sample Output 1:
----------------
[10, 20, 25, 30, 40]

Sample Input 2:
---------------
Enter a sorted list between:[]
[5, 15, 25, 35]
Enter number:
2

Sample Output 2:
----------------
[2, 5, 15, 25, 35]
'''

# Program Code
lst = eval(input("Enter a sorted list between:[] \n"))
n = int(input("Enter number: "))

for i in range(len(lst)):
    if n < lst[i]:
        lst.insert(i, n)
        break
else:
    lst.append(n)

print(lst)



# Mini-Max Sum (HackerRank)
# ------------------------

'''
Problem Statement:
------------------
Given five positive integers, find the minimum and maximum values
that can be calculated by summing exactly four of the five integers.
Print the respective minimum and maximum values as a single line
of two space-separated integers.

Example:
--------
arr = [1, 3, 7, 5, 9]

Minimum sum:
------------
Sum of all elements except the maximum value
= 1 + 3 + 5 + 7 = 16

Maximum sum:
------------
Sum of all elements except the minimum value
= 3 + 7 + 5 + 9 = 24

Expected Output:
----------------
16 24
'''

# Program Code
arr = [1, 3, 7, 5, 9]

min_sum = sum(arr) - max(arr)
max_sum = sum(arr) - min(arr)

print(min_sum, max_sum)




# Find Minimum and Maximum Element in a List
# -----------------------------------------

'''
Problem Statement:
------------------
Write a Python program to find the minimum and maximum elements
in a given list of integers without using built-in min() and max() functions.

Input Format:
-------------
The input consists of a single line containing space-separated integers.

Output Format:
--------------
Print the minimum element in the first line.
Print the maximum element in the second line.

Sample Input:
-------------
10 45 3 89 21

Sample Output:
--------------
3
89
'''

# Program Code
lst = list(map(int, input().rstrip().split()))

min_value = lst[0]
max_value = lst[0]

for i in lst[1:]:
    if i < min_value:
        min_value = i
    if i > max_value:
        max_value = i

print(min_value)
print(max_value)


# Find Length of a List Without Using len()
# ----------------------------------------

'''
Problem Statement:
------------------
Write a Python program to find the length of a list
without using the built-in len() function.

Input Format:
-------------
The input consists of a single line containing
space-separated integers.

Output Format:
--------------
Print the length of the list.

Sample Input:
-------------
10 20 30 40 50

Sample Output:
--------------
length of the list is: 5
'''

# Program Code
lst = list(map(int, input().rstrip().split()))

count = 0
for i in lst:
    count = count + 1

print(f"length of the list is: {count}")



# Find Sum of Elements in a List Without Using sum()
# ------------------------------------------------

'''
Problem Statement:
------------------
Write a Python program to find the sum of all elements
in a given list without using the built-in sum() function.

Input Format:
-------------
The input consists of a single line containing
space-separated integers.

Output Format:
--------------
Print the sum of the list elements.

Sample Input:
-------------
10 20 30 40

Sample Output:
--------------
100
'''

# Program Code
lst = list(map(int, input().rstrip().split()))

total = 0
for i in lst:
    total = total + i

print(f"sum of elements in a list is: {total}")




# Comparison Operators on Lists (==, !=, <, >, <=, >=)
# --------------------------------------------------

'''
Problem Statement:
------------------
Write a Python program to compare two lists using comparison operators.

Python compares lists **element by element** (lexicographical comparison),
similar to dictionary word comparison.

Input Format:
-------------
The first line contains space-separated integers for list1.
The second line contains space-separated integers for list2.

Output Format:
--------------
Print the result of comparing list1 and list2 using '<' operator.
(The output will be either True or False.)

Sample Input 1:
---------------
Enter list1 elements:
10 20 30
Enter list2 elements:
10 25 30

Sample Output 1:
----------------
True

Explanation:
------------
Comparison starts from index 0:
10 == 10 → move to next
20 < 25  → True (comparison stops here)
'''

# Program Code
lst1 = list(map(int, input("Enter list1 elements: ").rstrip().split()))
lst2 = list(map(int, input("Enter list2 elements: ").rstrip().split()))

print(lst1 < lst2)



