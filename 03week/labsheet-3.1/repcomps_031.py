#!/usr/bin/env python3

import sys

def multiples(numbers):
  replaced_list = [str(n).replace(str(n), "X") if n % 3 == 0 else n for n in numbers]
  return "Multiples of 3 replaced: " + str(replaced_list)

for num in sys.stdin:
  num = int(num)
  nums_list = list(range(1, num + 1))
  print (multiples(nums_list))
