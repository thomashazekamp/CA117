#!/usr/bin/env python3

import sys


censored_words = []
with open(sys.argv[1]) as f:
  for line in f:
    censored_words.append(line.strip())

for line in sys.stdin:
  line = line.strip()
  for c in censored_words:
    if c in line.lower():
      line = line.replace(c, '@' * len(c))
  print (line)
