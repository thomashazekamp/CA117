#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()

i = 1
long_word = input[0]
while i < len(input):
  if len(input[i]) > len(long_word):
    long_word = input[i]
  i = i + 1
long_word = len(long_word) - 1  # To remove the \n from the total count
# print (long_word)
for line in input:
  line = line.strip()
  print (f"{line:^{long_word}}")
