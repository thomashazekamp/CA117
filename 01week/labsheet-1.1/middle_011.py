#!/usr/bin/env python3

import sys
input = sys.stdin.read().strip().split()

#i = 0
#while i < len(input):
#  word = input[i]
#  if len(word) % 2 != 0:
#    mid_letter = word[len(word) // 2]
#    print (mid_letter)
#  else:
#    print ("No middle character!")
#  i = i + 1

for word in input:
  if len(word) % 2 != 0:
    mid_letter = word[len(word) // 2]
    print (mid_letter)
  else:
    print ("No middle character!")
