#!/usr/bin/env python3

import sys

content = sys.stdin.read()
content = content.strip().split()

numbers = content.copy()
numbers.pop(3)

ints = [int(item) for item in numbers]
ints.sort()
letters = content[-1]

A = ints[0]
B = ints[1]
C = ints[2]

letters = letters.replace("A", str(A) + " ", 1)
letters = letters.replace("B", str(B) + " ", 1)
letters = letters.replace("C", str(C) + " ", 1)
#  letters = [d for d in str(letters)]
#  print (" ".join(letters))
print (letters.rstrip())
