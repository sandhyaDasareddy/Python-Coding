'''
1. Program to print below pattern

Test case-1:
------------
Input:
Enter number:  5

Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

n = int(input("Enter number: "))

for i in range(n):
    print("* " * n)


'''
2. Program to print below pattern

Test case-1:
------------
Input:
Enter value of n: 5

Output:
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''

n = int(input("Enter value of n: "))

for i in range(1, n + 1):
    print((str(i) + " ") * n)


'''
3. Program to print below pattern

Input:
Enter number: 5

Output:
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

n = int(input("Enter number: "))

for i in range(n):
    print(*range(1, n + 1))


'''
4. Program to print below pattern

Input:
Enter number: 5

Output:
*
* *
* * *
* * * *
* * * * *
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    print("* " * i)

'''
5. Program to print below pattern

Input:
Enter number: 5

Output:
        *
      * *
    * * *
  * * * *
* * * * *
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

'''
6. Program to print below pattern

Input:
Enter number: 5

Output:
    *
   * *
  * * *
 * * * *
* * * * *
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

'''
7. Program to print below pattern

Input:
Enter number: 5

Output:
*****
 ****
  ***
   **
    *
'''

n = int(input("Enter number: "))

for i in range(n):
    print(" " * i + "*" * (n - i))


'''
8. Program to print below pattern

Input:
Enter number: 5

Output:
* * * * *
 * * * *
  * * *
   * *
    *
'''

n = int(input("Enter number: "))

for i in range(n):
    print(" " * i + "* " * (n - i))


'''
9. Program: Print Diamond Pattern

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

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
