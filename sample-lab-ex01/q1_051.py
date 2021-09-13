#!/usr/bin/env python3

import sys

#def swapped(s):
#  if len(s) == 1:
#    return ''.join(s)
#  if len(s) % 2 == 0:
#    for c in range(0, len(s), 2):
#      temp = s[c]
#      s[c] = s[c + 1]
#      s[c + 1] = temp
#    return ''.join(s)
#  if len(s) % 2 != 0:
#    for c in range(0, (len(s) - 1), 2):
#      temp = s[c]
#      s[c] = s[c + 1]
#      s[c + 1] = temp
#    return ''.join(s)
#
for line in sys.stdin:
  l = list(line.strip())
#  print (swapped(l))
  i = 1
  while i < len(l):
    l[i - 1], l[i] = l[i], l[i - 1]
    i = i + 2
  print (''.join(l))
