#!/usr/bin/env python3

import sys
input = sys.stdin.read().strip().split()

#i = 0
#while i < len(input):
#  word = input[i]
#  cut_word = word[1:len(word) - 1]
#  if len(cut_word) > 0:
#    print (cut_word)
#  i = i + 1
for word in input:
  cut_word = word[1:len(word) - 1]
  if len(cut_word) > 0:
    print (cut_word)
