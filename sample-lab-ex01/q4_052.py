#!/usr/bin/env python3

import sys

cal_d = {}
filename = sys.argv[1]
with open(filename, 'r') as f:
  for line in f:
    line = line.strip().split()
    key, value = ' '.join(line[:-1]), line[-1]
    cal_d[key] = value

tot_d = {}

for line in sys.stdin:
  line = line.strip().split(',')
  name, foods = line[0], line[1:]
  total = 0
  for f in foods:
    if f not in cal_d:
      cal_d[f] = '100'
    total = total + int(cal_d[f])
  tot_d[name] = total

sorted_dn = dict(sorted(tot_d.items(), key=lambda value: value[1]))
num_len = len(str(list(sorted_dn.values())[-1]))
word_len = len(sorted(tot_d.keys(), key=len)[-1])

for key, value in sorted_dn.items():
  print (f'{key:>{word_len}} : {value:{num_len}}')
