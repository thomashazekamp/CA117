#!/usr/bin/env python3

import sys

def main():
  for line in sys.stdin:
    line = line.strip()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for c in line.lower():
      if c in alpha:
        alpha = alpha.replace(c, '')
    if alpha == '':
      print ('pangram')
    else:
      print (f'missing {alpha}')

if __name__ == '__main__':
  main()
