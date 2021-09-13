#!/usr/bin/env python3

import sys

d = {}

with open(sys.argv[1], 'r') as f:
  f = f.readlines()
  i = 0
  for line in f:
    d[str(i)] = (line.strip().split()[0], line.strip().split()[1])
    i = i + 1

lines = sys.stdin.readlines()
for line in lines:
  word_nums = []
  nums = line.strip().split()
  for num in nums:
    word_nums.append(d[num][1])
  print (' '.join(word_nums))
