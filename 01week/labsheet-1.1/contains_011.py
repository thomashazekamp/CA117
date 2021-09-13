#!/usr/bin/env python3

import sys

count = 0
for line in sys.stdin:
  line = line.strip().lower()
  words = line.split()
  for char in words[0]:
    if char in words[1]:
      words[1] = words[1].replace(char, "", 1)
      count = count + 1
    else:
      print (False)
      count = 0
      break
    if count == len(words[0]):
      print (True)
      count = 0
