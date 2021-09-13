#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
numbers = lines[0].strip()
sequence = lines[1].strip()

nums_list = [int(n) for n in numbers.split()]
numbers = sorted(nums_list)
d, c, b, a = numbers

d = {'A': a, 'B': b, 'C': c, 'D': d}

print (' '.join([str(d[c]) for c in sequence]))
