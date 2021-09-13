#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()
  line_words = line.split()
  new_line = ""
  for word in line_words:
    word = word[:len(word) - 1] + word[len(word) - 1].capitalize()
    new_line = new_line + " " + word
  print (new_line.lstrip())
