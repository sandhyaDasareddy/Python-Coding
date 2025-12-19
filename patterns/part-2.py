'''
2. Program: Print Odd Star Triangle Pattern

Input:
Enter number: 5

Output:
*
* * *
* * * * *
* * * * * * *
* * * * * * * * *
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

'''
3. Program: Print Increasing Odd Number Pattern

Input:
Enter number: 5

Output:
1
1 2 3
1 2 3 4 5
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    for j in range(1, 2 * i):
        print(j, end=" ")
    print()

'''
4.a) Question:
------------
Write a program to print a centered pyramid pattern using stars.

Input:
Enter number: 5

Output:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, 2 * i):
        print("*", end=" ")
    print()


'''
4.b) Question:
---------
Write a program to print an inverted centered star pyramid
(reverse of a normal pyramid).

Input:
Enter number: 5

Output:
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

n = int(input("Enter number: "))

for i in range(n, 0, -1):
    # Print leading spaces
    for s in range(n - i):
        print(" ", end=" ")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

'''
5. Question:
------------
Write a program to print a number pyramid pattern where numbers increase
from 1 to the row number and then decrease back to 1.

Input:
------
Enter number: 5

Output:
-------
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    count = 1
    for j in range(1, 2 * i):
        if j < i:
            print(count, end=" ")
            count += 1
        else:
            print(count, end=" ")
            count -= 1
    print()

"""
6. Question:
------------
Write a program to print the following number pyramid pattern.

Input:
------
Enter number: 4

Output:
-------
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
"""

n = int(input("Enter number: "))

for i in range(1, n + 1):
    # printing leading spaces
    for k in range(1, n - i + 1):
        print(" ", end=" ")

    count = 1
    # printing numbers
    for j in range(1, 2 * i):
        if j < i:
            print(count, end=" ")
            count = count + 1
        else:
            print(count, end=" ")
            count = count - 1
    print()


'''
7. Question:
------------
Write a program to print the following pattern based on the given input.

Input:
------
Enter number: 4

Output:
-------
2 1 1 1 1
2 2 2 2 3
4 3 3 3 3
4 4 4 4 5
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    # If row is odd → print (i+1) at beginning
    if i % 2 != 0:
        print(i + 1, end=" ")

    # Print row number n times
    for j in range(n):
        print(i, end=" ")

    # If row is even → print (i+1) at end
    if i % 2 == 0:
        print(i + 1, end=" ")

    print()


'''
8. Question:
-----------
Write a program to print the following number pattern.
First, print numbers in increasing order where each row contains the same number.
Then, print numbers in decreasing order in the same format.

Input:
------
Enter number: 4

Output:
-------
1
2 2
3 3 3
4 4 4 4
3 3 3
2 2
1
'''

n = int(input("Enter number: "))

# Increasing pattern
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

# Decreasing pattern
for i in range(n - 1, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()


"""
9. Question:
-----------
Write a program to print a number pattern where each row prints the same
number repeatedly, starting from (n-1) down to 1.
The first row (n times n) should NOT be printed.

Input:
------
Enter number: 4

Output:
-------
4 4 4 4
3 3 3
2 2
1
"""

n = int(input())

for i in range(n - 1, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()



'''
10. Program: Right-aligned diamond-like star pattern

Input:
Enter number: 5

Output:
        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *
'''

n = int(input("Enter number: "))

# Increasing part
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

# Decreasing part (excluding middle row)
for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * i)


'''
11. Question:
------------
Write a program to print a diamond-like star pattern.
First, print stars in increasing order.
Then, print stars in decreasing order (excluding the middle row).

Input:
------
Enter number: 5

Output:
-------
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

n = int(input("Enter number: "))

# Increasing star pattern
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Decreasing star pattern (excluding middle row)
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


'''
12. Question:
------------
Write a program to print a symmetric diamond star pattern.
The pattern should first increase from 1 star up to N stars,
and then decrease back to 1 star, with proper left alignment
using spaces.

Input:
------
Enter number: 5

Output:
-------
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

n = int(input("Enter number: "))

# Upper half (including middle row)
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()

# Lower half (excluding middle row)
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()
