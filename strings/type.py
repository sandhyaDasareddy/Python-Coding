"""
========================================================
        PYTHON STRINGS – EFFICIENT & OPTIMIZED CODE
        (Basic → Advanced, Exam / CRT Ready)
========================================================
"""

# ======================================================
# 1. WHAT IS A STRING?
# ======================================================

'''
Any sequence of characters enclosed within
single quotes or double quotes is called a string.
'''

# ======================================================
# 2. STRING SLICING – CASE STUDY
# ======================================================

s = "abcdefghij"

print(s[1:6:2])      # bdf
print(s[::1])        # abcdefghij
print(s[::-1])       # jihgfedcba
print(s[7:4:-1])     # hgf
print(s[-4:1:-1])    # gfedc
print(s[-4:1:-2])    # gec
print(s[0:10000])    # abcdefghij
print(s[10000:2:-1]) # jihgfed

# ======================================================
# 3. ACCESS STRING (FORWARD & BACKWARD)
# ======================================================

s = "Learning Python is very easy !!!"

for ch in s:
    print(ch, end=" ")
print()

for ch in s[::-1]:
    print(ch, end=" ")
print()

# ======================================================
# 4. STRING COMPARISON
# ======================================================

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 == s2:
    print("Equal")
elif s1 < s2:
    print("First is smaller")
else:
    print("First is greater")

# ======================================================
# 5. REPLACE ALL OCCURRENCES
# ======================================================

print("ababab".replace("a", "b"))

# ======================================================
# 6. COUNT UPPER, LOWER, DIGIT, SPECIAL (NO SPACE)
# ======================================================

s = input("Enter string: ")

uc = lc = dc = sc = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        uc += 1
    elif 'a' <= ch <= 'z':
        lc += 1
    elif '0' <= ch <= '9':
        dc += 1
    elif ch != ' ':
        sc += 1

print("Upper:", uc)
print("Lower:", lc)
print("Digits:", dc)
print("Special:", sc)

# ======================================================
# 7. LOWER → UPPER
# ======================================================

print(input("Enter string: ").upper())

# ======================================================
# 8. UPPER → LOWER
# ======================================================

print(input("Enter string: ").lower())

# ======================================================
# 9. CAPITALIZE EACH WORD
# ======================================================

print(input("Enter string: ").title())

# ======================================================
# 10. CAPITALIZE FIRST LETTER ONLY
# ======================================================

print(input("Enter string: ").capitalize())

# ======================================================
# 11. SWAP CASE
# ======================================================

print(input("Enter string: ").swapcase())

# ======================================================
# 12. CHECK UPPERCASE CHARACTER
# ======================================================

ch = input("Enter character: ")
print("Uppercase" if 'A' <= ch <= 'Z' else "Not Uppercase")

# ======================================================
# 13. CHECK DIGIT
# ======================================================

ch = input("Enter character: ")
print("Digit" if '0' <= ch <= '9' else "Not Digit")

# ======================================================
# 14. CHECK WORD "python" PRESENT OR NOT
# ======================================================

s = input("Enter string: ")
print("Found" if "python" in s.lower() else "Not Found")

# ======================================================
# 15. REPLACE 'a' WITH "hello"
# ======================================================

print(input("Enter string: ").replace("a", "hello"))

# ======================================================
# 16. REMOVE ALL SPACES
# ======================================================

print(input("Enter string: ").replace(" ", ""))

# ======================================================
# 17. index() vs find()
# ======================================================

s = "python"
print(s.find("z"))   # -1
# s.index("z")       # ValueError

# ======================================================
# 18. CHARACTERS AT EVEN & ODD POSITIONS
# ======================================================

s = input("Enter string: ")
print("Even:", s[0::2])
print("Odd :", s[1::2])

# ======================================================
# 19. MERGE TWO STRINGS ALTERNATIVELY
# ======================================================

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

res = ""
for i in range(max(len(s1), len(s2))):
    if i < len(s1): res += s1[i]
    if i < len(s2): res += s2[i]

print(res)

# ======================================================
# 20. a4b3c2 → aaaabbbcc
# ======================================================

s = "a4b3c2"
res = ""

for i in range(0, len(s), 2):
    res += s[i] * int(s[i+1])

print(res)

# ======================================================
# 21. a4k3b2 → aeknbd
# ======================================================

s = "a4k3b2"
res = ""

for i in range(0, len(s), 2):
    res += chr(ord(s[i]) + int(s[i+1]))

print(res)

# ======================================================
# 22. REMOVE DUPLICATES (ORDER PRESERVED)
# ======================================================

s = "ABCDABBCDABBBCCCDDEEEF"
res = ""

for ch in s:
    if ch not in res:
        res += ch

print(res)

# ======================================================
# 23. REVERSE ALTERNATE WORDS
# ======================================================

s = "one two three four five six seven"
words = s.split()

for i in range(1, len(words), 2):
    words[i] = words[i][::-1]

print(" ".join(words))
