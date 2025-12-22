# zip() Function Example
# ---------------------

'''
Problem Statement:
------------------
Write a Python program to combine two lists element-wise
using the zip() function.

Input:
------
Two predefined lists of integers.

Output:
-------
Print a list of tuples where each tuple contains
one element from each list at the same index.

Sample Input:
-------------
list1 = [5, 12, 17, 7]
list2 = [15, 8, 15, 3]

Sample Output:
--------------
[(5, 15), (12, 8), (17, 15), (7, 3)]
'''

# Program Code
lst1 = [5, 12, 17, 7]
lst2 = [15, 8, 15, 3]

res = list(zip(lst1, lst2))

print(res)
#---------------------------------------------------------------------------------------------------


# zip() Function with for loop
# ---------------------------

'''
Problem Statement:
------------------
Write a Python program to iterate over two lists
simultaneously using the zip() function and print
their elements pair-wise.

Input:
------
Two predefined lists of integers.

Output:
-------
Print elements from both lists in pair form
(one pair per line).

Sample Input:
-------------
list1 = [5, 12, 17, 7]
list2 = [15, 8, 15, 3]

Sample Output:
--------------
5 15
12 8
17 15
7 3
'''

# Program Code
lst1 = [5, 12, 17, 7]
lst2 = [15, 8, 15, 3]

for i, j in zip(lst1, lst2):
    print(i, j)
#---------------------------------------------------------------------------------------------------


# String Concatenation Using zip()
# -------------------------------

'''
Problem Statement:
------------------
Write a Python program to concatenate elements of two lists
string by string using the zip() function.

Input:
------
Two predefined lists of strings of equal length.

Output:
-------
Print the concatenated strings in a single line,
separated by spaces.

Sample Input:
-------------
lst1 = ["A","app","","da","kee","t","doc","a"]
lst2 = ["n","le","a","y","ps","he","tor","way"]

Sample Output:
--------------
An apple a day keeps the doctor away
'''

# Program Code
lst1 = ["A", "app", "", "da", "kee", "t", "doc", "a"]
lst2 = ["n", "le", "a", "y", "ps", "he", "tor", "way"]

res = []
for i, j in zip(lst1, lst2):
    res.append(i + j)

print(' '.join(res))

#---------------------------------------------------------------------------------------------------


