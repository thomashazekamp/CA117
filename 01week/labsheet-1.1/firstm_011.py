#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()
  words = line.split()
  i = 0
  while i < len(words):
    if words[i].startswith("m"):
      words[i] = words[i].capitalize()
      break
    i = i + 1
  print (" ".join(words))
