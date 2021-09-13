#!/usr/bin/env python3

import sys

def calc_roots(a, b, c):
  if ((b ** 2) - (4 * a * c)) < 0:
    return None
  else:
    disc = (b ** 2) - (4 * a * c)
    r1 = (-b + (disc ** (1 / 2))) / (2 * a)
    r2 = (-b - (disc ** (1 / 2))) / (2 * a)
    return r1, r2

def main():
  for line in sys.stdin:
    line_list = line.strip().split()
    nums = [int(n) for n in line_list]
    [a, b, c] = nums
    checker = calc_roots(a, b, c)
   # print (checker)
    if checker is None:
      print ('None')
    else:
      r1, r2 = checker
      print (f'r1 = {r1}, r2 = {r2}')


if __name__ == '__main__':
  main()
