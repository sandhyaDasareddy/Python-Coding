# Count of occurrences of each character

str = input("Enter your name: ")
d = {}

# Converting string to uppercase and counting characters
for i in str.upper():
    if i not in d:
        d[i] = 1        # First occurrence
    else:
        d[i] = d[i] + 1  # Increment count

# Printing the dictionary
print(d)
#--------------------------------------------------------------------------

# Number of pairs in a given list
lst = list(map(int, input("Enter your values: ").split()))

d = {}

# Counting frequency of each element
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

# Calculating total number of pairs
res = 0
for i in d.values():
    res = res + i // 2

# Printing the result
print(res)
#--------------------------------------------------------------------------

# Write a program to print the mobile number associated with the name
# If the name is not found, display "No contact found"

n = int(input())
d = {}

# Reading name and mobile number
for i in range(n):
    l = input().split()
    d[l[0]] = l[1]

s = int(input())

# Searching for the given names
for i in range(s):
    name = input()
    if name in d:
        print("mobile no:", d[name])
    else:
        print("No contact found")
#--------------------------------------------------------------------------

# Write a program to print the kth non-repeating character in the given string
# Input:
# comprehension
# 3
# Output:
# m

lst = input()
k = int(input())

d = {}

# Count frequency of each character
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

count = 0

# Find kth non-repeating character
for i in d:
    if d[i] == 1:
        count += 1
        if count == k:
            print(i)
            break
#--------------------------------------------------------------------------

#Program to Print Words Occurring 3 or More Times in a Sentence
# 'That that is is that that is not is not. is that it? it is.'

import re

lst = input().upper()
lst = re.sub(r"[.,?!!@#$%^&*:'\"+=}{|><]", "", lst).split()

d = {}

# Counting frequency of each word
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

# Printing words occurring 3 or more times
for i in d:
    if d[i] >= 3:
        print(i, ":", d[i])
#--------------------------------------------------------------------------


