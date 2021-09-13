#!/usr/bin/env python3

import sys
t = "Multiples of 3: "
ts = "Multiples of 3 squared: "
df = "Multiples of 4 doubled: "
torf = "Multiples of 3 or 4: "
tandf = "Multiples of 3 and 4: "

def multiples(numbers):
  multi_t = [n for n in numbers if n % 3 == 0]
  multi_ts = [n ** 2 for n in numbers if n % 3 == 0]
  multi_df = [n * 2 for n in numbers if n % 4 == 0]
  multi_torf = [n for n in numbers if n % 3 == 0 or n % 4 == 0]
  multi_tandf = [n for n in numbers if n % 3 == 0 and n % 4 == 0]
  print (t + str(multi_t))
  print (ts + str(multi_ts))
  print (df + str(multi_df))
  print (torf + str(multi_torf))
  return tandf + str(multi_tandf)

for num in sys.stdin:
  num = int(num)
  nums_list = list(range(1, num + 1))
  print (multiples(nums_list))
