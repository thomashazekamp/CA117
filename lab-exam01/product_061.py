#!/usr/bin/env python3

import sys

def main():
  for line in sys.stdin:
    line_list = list(line.strip())
    product_list = [int(n) for n in line_list if int(n) != 0]
    prod = 1
    for n in product_list:
      prod = prod * n

    while prod % 10 != 0 and prod > 9:
      line_list = list(str(prod))
      product_list = [int(n) for n in line_list if int(n) != 0]
      prod = 1
      for n in product_list:
        prod = prod * n

    if prod % 10 == 0:
      product_str = int(list(str(prod))[0])
      print (product_str)
    else:
      print (prod)


if __name__ == '__main__':
  main()
