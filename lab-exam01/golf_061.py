#!/usr/bin/env python3

import sys

def checker(n):
  return n >= 0

def sorter(t):
  return t[-1]

def main():
  d = {}
  disqual = []
  for line in sys.stdin:
    try:
      tokens = line.strip().split()
      name, shots = ' '.join(tokens[:-3]), tokens[-3:]
      for i in shots:
        if checker(int(i)) is False:
          raise ValueError
      sum_shots = sum([int(n) for n in shots])
      d[name] = sum_shots
    except ValueError:
      disqual.append(name)
      continue

  for key, value in sorted(d.items(), key=sorter):
    print (f'{key}: {value}')
  if len(disqual) > 0:
    dis_str = ', '.join(disqual)
    print (f'Disqualified: {dis_str}')

if __name__ == '__main__':
  main()
