#!/usr/bin/env python3

import sys

def check(s):
  l = ['e', 'v', 'i', 'l']
  for c in s.lower():
    if c not in l:
      s = s.lower().replace(c, '')
  return s.lower() == 'evil'

for line in sys.stdin:
  line = line.strip()
  if check(line) is True:
    print (line)
