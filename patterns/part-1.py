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
    for j in range(n):
        print("*", end=" ")
    print()


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
    for j in range(n):
        print(i, end=" ")
    print()

'''
3. Program to print below pattern

Input:
Enter number:  5

Output:
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

n = int(input("Enter number: "))

for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()


'''
4. Program to print below pattern

Input:
Enter number:  4

Output:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''

n = int(input("Enter number: "))

count = 1

for i in range(n):
    for j in range(n):
        print(count, end=" ")
        count += 1
    print()


'''
5. Program to print below pattern

Input:
Enter number: 4

Output:
1 5 9 13
2 6 10 14
3 7 11 15
4 8 12 16
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    for j in range(i, n * n + 1, n):
        print(j, end=" ")
    print()


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
    for j in range(i):
        print("*", end=" ")
    print()


'''
7. Program to print below pattern

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
    for space in range(n - i):
        print(" ", end=" ")
    for star in range(i):
        print("*", end=" ")
    print()


'''
8. Program to print below pattern (Hollow Square)

Input:
Enter number: 5

Output:
* * * * *
*       *
*       *
*       *
* * * * *
'''

n = int(input("Enter number: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


'''
9. Program to print below pattern

Input:
Enter number: 5

Output:
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()


'''
10. Program Name: Number Right-Angled Triangle Pattern

Input:
Enter number: 5

Output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()


'''
11. Program Name: Right-Aligned Star Triangle Pattern

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
    for space in range(n - i):
        print(" ", end="")
    for star in range(i):
        print("* ", end="")
    print()


'''
12. Program Name: Inverted Number Triangle Pattern

Input:
Enter number: 5

Output:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

n = int(input("Enter number: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        print(j, end=" ")
    print()
