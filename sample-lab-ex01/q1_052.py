#!/usr/bin/env python3

import sys

def rotation(s, n):
  n = int(n) % len(s)
  new_s = s[(len(s) - n):] + s[0:(len(s) - n)]
  return new_s

for line in sys.stdin:
  string, times = line.strip().split()
  print (rotation(string, times))
