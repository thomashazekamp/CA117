#!/usr/bin/env python3

import sys
from math import pi

for num in sys.stdin:
  num = int(num)
  print (f"{pi:.{num}f}")
