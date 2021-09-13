#!/usr/bin/env python3

import sys

input = sys.stdin.read().lower().strip()
def main():
  dict_count = {
    'a': input.count('a'),
    'e': input.count('e'),
    'i': input.count('i'),
    'o': input.count('o'),
    'u': input.count('u')
  }
  return dict_count

sorted_value = sorted(main().items(), key=lambda x: x[1], reverse=True)
long_digit = len(str(sorted_value[0][1]))
for k, v in sorted_value:
  print (f'{k} : {v:>{long_digit}}')
