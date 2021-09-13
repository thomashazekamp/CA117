#!/usr/bin/env python3

import sys

def palin():
  if joint == joint[::-1]:
    return True
  else:
    return False

for line in sys.stdin:
  line = line.strip().lower()
  for c in line:
    if c.isalnum() is True or c.isspace() is True:
      pass
    else:
      line = line.replace(c, "", 1)
  line = line.split()
  joint = "".join(line)
  print (palin())
