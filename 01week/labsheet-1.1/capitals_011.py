#!/usr/bin/env python3

import sys
input = sys.stdin.read().strip().split()

#i = 0
#while i < len(input):
#  word = input[i]
#  if len(word) > 1:
#    cap_word = word[0].capitalize() + word[1:len(word) - 1] + word[len(word) - 1].capitalize()
#    print (cap_word)
#  i = i + 1

for word in input:
  if len(word) > 1:
    cap_word = word[0].capitalize() + word[1:len(word) - 1] + word[len(word) - 1].capitalize()
    print (cap_word)
