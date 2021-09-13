#!/usr/bin/env python3

import sys

d = {
  '0': 'zero',
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine',
  '10': 'ten'
    }

lines = sys.stdin.readlines()
for line in lines:
  word_nums = []
  nums = line.strip().split()
  for num in nums:
    word_nums.append(d[num])
  print (' '.join(word_nums))
