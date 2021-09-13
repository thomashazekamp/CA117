#!/usr/bin/env python3

import sys

import time

def sumFac(n):
  num_tot = 1
  i = 2
  while i * i <= n:
    if n % i == 0:
      num_tot = num_tot + i + n / i
    i = i + 1
  return num_tot

def isPerfect(n, sn):
  return n == sn and n != 1

def main():
  for line in sys.stdin:
    num = int(line.strip())
    num_sum = sumFac(num)
    print (isPerfect(num, num_sum))

#start_time = time.time()
#print ('--- %s seconds ---' % (time.time() - start_time))

if __name__ == '__main__':
  main()
