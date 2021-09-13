#!/usr/bin/env python3

import sys

def binsearch(query, sorted_list):
  low = 0
  high = len(sorted_list) - 1
  while low <= high:
    mid = (low + high) // 2
    if sorted_list[mid] < query:
      low = mid + 1
    elif sorted_list[mid] > query:
      high = mid - 1
    else:
      return True
  return False
list = [line.strip() for line in sys.stdin]

slist = sorted([w.lower() for w in list])

revs = [w for w in list if len(w) >= 5 and binsearch(w[::-1].lower(), slist)]

print (revs)
