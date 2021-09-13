#!/usr/bin/env python3

import sys

def sorter(t):
  return t[1]

def main():
  d = {}
  skips = []
  for line in sys.stdin:
    try:
      name, marks = line.strip().split(':')
      marks_list = marks.strip().split(',')
      mark = sum([int(m) for m in marks_list])
      d[name] = mark
    except ValueError:
      skips.append(name)

  for k, v in sorted(d.items(), key=sorter, reverse=True):
    print (f'{k:s} : {v:d}')

  print ('Skipped:')
  for name in skips:
    print (f'{name}')

if __name__ == '__main__':
  main()
