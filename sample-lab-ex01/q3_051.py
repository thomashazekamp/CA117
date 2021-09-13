#!/usr/bin/env python3

import sys

#for line in sys.stdin:
#  line = line.strip()
def check(s):
  for c in s:
    if c.islower() is True:
      s = s.replace(c, ' ')
  return sorted(s.split(), key=len, reverse=True)[0]

for line in sys.stdin:
  line = line.strip()
  print (check(line))
