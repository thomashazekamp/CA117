#!/usr/bin/env python3

import sys

for noun in sys.stdin:
  noun = noun.strip()
  if noun.endswith(("ch", "sh", "x", "s", "z", "o")):
    noun = noun + "es"
    print (noun)
  elif noun.endswith(("f", "fe")):
    split = noun.rsplit("f", 1)
    noun = split[0] + "ves"
    print (noun)
  elif noun.endswith(("by", "cy", "dy", "fy", "gy", "hy", "jy", "ky", "ly", "my", "ny", "py", "qy", "ry", "sy", "ty", "vy", "wy", "xy", "zy")):
    split = noun.rsplit("y", 1)
    noun = split[0] + "ies"
    print (noun)
  else:
    print (noun + "s")

# to check for consonant, you can also check if there are no vowles (aeiou) if occurs remove "y" and add "ies"
# e.g
# start of code:
# vowels = "aeiou"
# if noun[-1] == "y" and noun[-2] not in vowels:
#   print (noun[:-1] + "ies")
