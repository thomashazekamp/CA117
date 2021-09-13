#!/usr/bin/env python3

import sys

def main():
  line1 = int(sys.stdin.readline().strip())
  line2 = sys.stdin.readline().strip()
  l = [int(n) for n in line2.split()]
  max_l = line1
  count = 0
  for n in l:
    if max_l > 0:
      max_l = max_l - n
      if max_l >= 0:
        count = count + 1
    else:
      break
  print (count)

if __name__ == '__main__':
  main()
