#!/usr/bin/env python3

import sys

def num():
  try:
    count = 0
    for line in sys.stdin:
      line = line.strip()
      if line.isdigit() is True and count == 0:
        print (f"Thank you for {line}")
        count += 1
      elif count == 1:
        break
      else:
        print (f"{line} is not a number")

  except FileNotFoundError:
    print (f"The file could not be opened")

num()
