#!/usr/bin/env python3

import sys
inputs = sys.stdin.readlines()

a = []  # New list of lines with all lower case

for line in inputs:
  line = line.strip()
  low_line = line.lower()
  a.append(low_line)

i = 0
while i < len(a):
  word = a[i].split()
  if word[0] in word[1]:
    print ("True")
  else:
    print ("False")
  i = i + 1
