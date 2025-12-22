# Traditional method
lst = [1 ,2, 5 , 6, 7, 8]
sq_lst = []
for i in lst:
    sq_lst.append(i**2)
print(lst)
print(sq_lst)
#---------------------------------------------------------------------------------------------------


# List Comprehension Example
# -------------------------

'''
Concept:
--------
List comprehension provides a concise way to create lists.

Syntax:
-------
[expression for item in iterable if condition]

[what i want From which loop on what condition](for user understand purpose)

Explanation:
------------
- expression : what you want to store in the new list
- item       : variable that takes each value from the iterable
- iterable   : list / tuple / range etc.
- condition  : (optional) filter condition

Problem Statement:
------------------
Write a Python program to create a new list containing
the squares of elements from an existing list using list comprehension.

Input:
------
A predefined list of integers.

Output:
-------
Print the original list and the list of squared elements.

Sample Input:
-------------
[1, 2, 5, 6, 7, 8]

Sample Output:
--------------
[1, 2, 5, 6, 7, 8]
[1, 4, 25, 36, 49, 64]
'''

# Program Code
lst = [1, 2, 5, 6, 7, 8]

sq_lst = [i**2 for i in lst]

print(lst)
print(sq_lst)
#---------------------------------------------------------------------------------------------------


# List Comprehension with Condition
# --------------------------------

'''
Problem Statement:
------------------
Write a Python program to create a new list containing
the squares of only even numbers from a given list
using list comprehension.

Syntax:
-------
[expression for item in iterable if condition]

Input:
------
A predefined list of integers.

Output:
-------
Print the list of squared even numbers.

Sample Input:
-------------
[1, 2, 5, 6, 7, 8]

Sample Output:
--------------
[4, 36, 64]
'''

# Program Code
lst = [1, 2, 5, 6, 7, 8]

even_sq_lst = [i**2 for i in lst if i % 2 == 0]

print(even_sq_lst)
#---------------------------------------------------------------------------------------------------


# List Comprehension with if–else (Conditional Expression)
# ------------------------------------------------------

'''
Problem Statement:
------------------
Write a Python program using list comprehension such that:
- If the element is even, store its square
- If the element is odd, store its double

Syntax:
-------
[expression_if_true if condition else expression_if_false for item in iterable]

Input:
------
A predefined list of integers.

Output:
-------
Print the resulting list.

Sample Input:
-------------
[1, 2, 5, 6, 7, 8]

Sample Output:
--------------
[2, 4, 10, 36, 14, 64]
'''

# Program Code
lst = [1, 2, 5, 6, 7, 8]

res = [i*i if i % 2 == 0 else i + i for i in lst]

print(res)
#---------------------------------------------------------------------------------------------------



# Program to Count Number of Vowels in a String
# --------------------------------------------

'''
Problem Statement:
------------------
Write a Python program to count the number of vowels
present in a given string.

Vowels:
-------
a, e, i, o, u (both uppercase and lowercase)

Approach:
---------
- Traverse each character in the string
- Check if it is present in the vowel set
- Store vowels in a list using list comprehension
- Count the length of the list

Input:
------
A predefined string.

Output:
-------
Print the number of vowels in the string.

Sample Input:
-------------
"india is my country"

Sample Output:
--------------
6
'''

# Program Code

print(len([i for i in "india is my country" if i in "aeiouAEIOU"]))

'''
s = "india is my country"
vowels = "aeiouAEIOU"
 or 
res = [i for i in s if i in vowels]

print(len(res))'''
#---------------------------------------------------------------------------------------------------


# Cartesian Product of Two Lists (Excluding Equal Pairs)
# ----------------------------------------------------

'''
Problem Statement:
------------------
Write a Python program to generate all possible pairs
(i, j) such that:
- i belongs to list1
- j belongs to list2
- i is not equal to j

Use list comprehension to solve the problem.

Input:
------
Two predefined lists of integers.

Output:
-------
Print a list of tuples containing all pairs
where the elements are not equal.

Sample Input:
-------------
list1 = [2, 4, 3]
list2 = [5, 2, 4, 1]

Sample Output:
--------------
[(2, 5), (2, 4), (2, 1),
 (4, 5), (4, 2), (4, 1),
 (3, 5), (3, 2), (3, 4), (3, 1)]
'''

# Program Code
l1 = [2, 4, 3]
l2 = [5, 2, 4, 1]
'''
l1 = [2,4,3]
l2 = [5,2,4,1]

for i in l1:
    for j in l2:
        if i != j:
            print(i, j, end=" ")
    print()

'''
result = [(i, j) for i in l1 for j in l2 if i != j]

print(result)
#---------------------------------------------------------------------------------------------------


# Generate Tuples with Cube Values
# -------------------------------

'''
Problem Statement:
------------------
Write a Python program to generate a list of tuples
containing a number and its cube from 1 to n.

Input Format:
-------------
The input consists of a single integer n.

Output Format:
--------------
Print a list of tuples in the form (i, i³) for
each value of i from 1 to n.

Sample Input:
-------------
5

Sample Output:
--------------
[(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]


program code:
-------------
n = int(input())
res = []
for i in range(1, n + 1):
    res.append((i, i**3))
print(res)
'''

# Program Code (List Comprehension)
print([(i, i**3) for i in range(1, int(input("Enter N: ")) + 1)])
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

lst1 = ["A", "app", "", "da", "kee", "t", "doc", "a"]
lst2 = ["n", "le", "a", "y", "ps", "he", "tor", "way"]

print(' '.join([i + j for i, j in zip(lst1, lst2)]))


#---------------------------------------------------------------------------------------------------


# Convert Words Based on Length
# ----------------------------

'''
Problem Statement:
------------------
Write a Python program to read a string and:
- Convert words with length greater than 5 to lowercase
- Convert words with length less than or equal to 5 to uppercase

Input Format:
-------------
The input consists of a single line string.

Output Format:
--------------
Print the modified string.

Sample Input:
-------------
Enter string:
Python is a Powerful Language

Sample Output:
--------------
PYTHON IS A powerful language

# Program Code
s = input("Enter string: ")
lst = s.split()
for i in lst:
    if len(i)>5:
        print(i.lower(),end=" ")
    else:
        print(i.upper(),end=" ")
'''
s = input("Enter string: ")

lst = s.split()

result = ' '.join([i.lower() if len(i) > 5 else i.upper() for i in lst])

print(result)
#---------------------------------------------------------------------------------------------------



# all() and any() Functions
# ------------------------

'''
Problem Statement:
------------------
Write a Python program to demonstrate the use of
all() and any() functions on a list of integers.

Conditions:
-----------
- all() returns True if all elements satisfy the condition
- any() returns True if at least one element satisfies the condition

Input:
------
Two predefined lists of integers.

Output:
-------
Print the result of all() and any() for each list.

Sample Input:
-------------
lst1 = [10, 20, -30, 40, 50, 60]
lst2 = [-10, -20, 30, -40, -50, -60]

Sample Output:
--------------
False
True
False
True
'''

# Program Code
lst = [10, 20, -30, 40, 50, 60]
print(all(i > 0 for i in lst))
print(any(i > 0 for i in lst))

lst = [-10, -20, 30, -40, -50, -60]
print(all(i > 0 for i in lst))
print(any(i > 0 for i in lst))
#---------------------------------------------------------------------------------------------------


# Student Pass Status Using all()
# -------------------------------

'''
Problem Statement:
------------------
Write a Python program to check whether a student
has passed in all subjects using the all() function.

Condition:
----------
- A student passes a subject if marks >= 35
- The student is considered passed only if all
  subject marks are >= 35

Input:
------
Two predefined lists containing marks of a student
in different subjects.

Output:
-------
Print True if the student has passed in all subjects,
otherwise print False.

Sample Input:
-------------
s1_marks = [56, 98, 67, 88, 35]
s1_marks = [56, 23, 67, 88, 35]

Sample Output:
--------------
True
False
'''

# Program Code
s1_marks = [56, 98, 67, 88, 35]
print(all(i >= 35 for i in s1_marks))

s1_marks = [56, 23, 67, 88, 35]
print(all(i >= 35 for i in s1_marks))


#---------------------------------------------------------------------------------------------------
# Checking High Score Using any()
# -------------------------------

'''
Problem Statement:
------------------
Write a Python program to check whether a student
has scored more than 70 marks in at least one subject
using the any() function.

Condition:
----------
- Score > 70 is considered a high score
- any() returns True if at least one subject
  satisfies the condition

Input:
------
A predefined list containing marks of a student
in different subjects.

Output:
-------
Print True if the student has scored more than
70 marks in any one subject, otherwise print False.

Sample Input:
-------------
s1_marks = [56, 98, 67, 88, 35]

Sample Output:
--------------
True
'''

# Program Code
s1_marks = [56, 98, 67, 88, 35]

print(any(i > 70 for i in s1_marks))
