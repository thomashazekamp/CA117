#!/usr/bin/env python3

import sys
from math import pi

def main():
  for line in sys.stdin:
    numbers = line.strip().split()
    start_r = float(numbers[0])
    inc_r = float(numbers[1])
    end_r = float(numbers[2])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print (f'{h1:>s} {h2:>15s} {h3:>15s}')
    print (f'{h4:>s} {h5:>15s} {h6:>15s}')
    area = 4 * pi * (start_r ** 2)
    volume = (4 / 3) * pi * (start_r ** 3)
    i = start_r
#   print (f"{1:>{10}.1f} {12.5733:>{15}.2f} {4.1922:>{15}.2f}") this is a testing case
    while i < (end_r + inc_r) and i < (end_r + (inc_r / 2)):
      print (f"{start_r:>{10}.1f} {area:>{15}.2f} {volume:>{15}.2f}")
      start_r = start_r + inc_r
      area = 4 * pi * (start_r ** 2)
      volume = (4 / 3) * pi * (start_r ** 3)
      i = i + inc_r

if __name__ == '__main__':
    main()
