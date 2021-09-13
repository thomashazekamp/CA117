#!/usr/bin/env python3

import sys
from string import punctuation

input = sys.stdin.read().lower().strip().split()

def main():
  dict = {}
  for a in input:
    a = a.rstrip(punctuation)
    if a not in dict:
      dict[a] = 1
    else:
      dict[a] = dict[a] + 1
  return dict

new_d = {}
for k, v in sorted(main().items()):
  if len(k) > 3 and v >= 3:
    new_d[k] = v

key_list = new_d.keys()
longestw = len(sorted(key_list, key=len)[-1])

values_list = new_d.values()
largestn = len(str(sorted(values_list)[-1]))

for k, v in new_d.items():
  print (f'{k:>{longestw}} : {v:>{largestn}}')
