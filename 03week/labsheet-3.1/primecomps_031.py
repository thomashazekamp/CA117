#!/usr/bin/env python3

import sys

for num in sys.stdin:
  num = int(num)
  numbers_list = list(range(1, num + 1))
  nonprime_list = []

  for n in numbers_list:
    for i in range(2, n):
      if n % i == 0:
        nonprime_list.append(n)
        break
  #  print (nonprime_list)
  primes = [n for n in numbers_list if n != 1 and n != 0 and n not in nonprime_list]
  print (f'Primes: {primes}')
