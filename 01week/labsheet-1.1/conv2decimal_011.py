#!/usr/bin/env python3

import sys

for numbers in sys.stdin:
  numbers = numbers.strip()
  num_split = numbers.split()
  base = num_split[1]
  num = num_split[0]
  conv = 0

  i = 1
  while i < (len(num) + 1):
    digit = num[len(num) - i]
    conv = conv + ((int(base) ** (i - 1)) * int(digit))
    i = i + 1
  print (conv)
