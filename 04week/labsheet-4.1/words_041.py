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
for k, v in sorted(main().items()):
  print (f'{k} : {v}')
