#/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()
  initial_cap = line.title()
  print (initial_cap)
