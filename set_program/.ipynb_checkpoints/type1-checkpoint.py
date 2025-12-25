# Remove Duplicate Programming Language Names
# ------------------------------------------
'''
Problem Statement:
------------------
Write a Python program to take programming language names
from the user and remove all duplicate entries.

Input Format:
-------------
The input consists of a single line containing
space-separated programming language names.

Output Format:
--------------
Print the list of language names and then print
the set after removing duplicates.

Note:
-----
- set() removes duplicate values
- Order of elements may change because sets are unordered
'''

# Program Code
lst = input("Enter programming language names: ").rstrip().split()
print("Original List:", lst)

# Removing duplicates using set
s = set(lst)
print("After removing duplicates:", s)
#-------------------------------------------------------------------------------------------------



# Count Number of Duplicate Elements in a List
# --------------------------------------------
'''
Problem Statement:
------------------
Write a Python program to count the number of duplicate
elements present in a list.

Input Format:
-------------
The input consists of a single line containing
space-separated integers.

Output Format:
--------------
Print the count of duplicate elements.

Logic:
------
- Convert the list into a set (removes duplicates)
- Subtract the length of the set from the length of the list

Formula:
--------
Number of duplicates = len(list) - len(set)

Sample Input:
-------------
10 20 30 20 40 10 50

Sample Output:
--------------
2
'''

# Program Code
lst = list(map(int, input().split()))

s = set(lst)

unique_elements = len(lst) - len(s)

print(unique_elements)
#-------------------------------------------------------------------------------------------------



# Count Number of Duplicate Elements in a List
# --------------------------------------------
'''
Problem Statement:
------------------
Write a Python program to count the number of duplicate
elements present in a list.

Input Format:
-------------
The input consists of a single line containing
space-separated integers.

Output Format:
--------------
Print the count of duplicate elements.

Logic:
------
- Convert the list into a set (removes duplicates)
- Subtract the length of the set from the length of the list

Formula:
--------
Number of duplicates = len(list) - len(set)

Sample Input:
-------------
10 20 30 20 40 10 50

Sample Output:
--------------
2
'''

# Program Code
lst = list(map(int, input().split()))

s = set(lst)

unique_elements = len(lst) - len(s)

print(unique_elements)
#-------------------------------------------------------------------------------------------------



# Set Operations – Sports Participation
# -------------------------------------
'''
Problem Statement:
------------------
Given three sets of roll numbers of students who play:
- Hockey
- Football
- Cricket

Print the roll numbers of students according to the following conditions:
1) Students who play any game
2) Students who play all three games
3) Students who play only hockey
4) Students who play either football or cricket but not both
'''

# Sets of roll numbers
h = {1, 9, 12, 7, 14}                  # Hockey
f = {6, 9, 8, 10, 5, 11, 12, 13, 15}   # Football
c = {2, 4, 9, 3, 5, 13}                # Cricket

print("Hockey:", h)
print("Football:", f)
print("Cricket:", c)

# 1) Students who play any game (Union)
print("\n1) Students who play any game:")
print(h | f | c)

# 2) Students who play all three games (Intersection)
print("\n2) Students who play all three games:")
print(h & f & c)

# 3) Students who play only hockey
print("\n3) Students who play only hockey:")
print(h - (f | c))

# 4) Students who play either football or cricket but not both
print("\n4) Students who play either football or cricket but not both:")
print(f ^ c)
