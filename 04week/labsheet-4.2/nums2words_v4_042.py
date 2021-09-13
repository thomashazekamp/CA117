#!/usr/bin/env python3

import sys

d = {
  '0': 'zero',
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine',
  '10': 'ten',
  '11': 'eleven',
  '12': 'twelve',
  '13': 'thirteen',
  '14': 'fourteen',
  '15': 'fifteen',
  '16': 'sixteen',
  '17': 'seventeen',
  '18': 'eighteen',
  '19': 'nineteen',
  '20': 'twenty',
  '30': 'thirty',
  '40': 'forty',
  '50': 'fifty',
  '60': 'sixty',
  '70': 'seventy',
  '80': 'eighty',
  '90': 'ninety',
  '100': 'one hundred'
    }

for line in sys.stdin:
  word_nums = []
  nums = line.strip().split()
  for n in nums:
    if n in d:
      word_nums.append(d[n])
    elif len(n) == 2:
      second_digit = int(n[1])
      first_word_num = str(int(n) - second_digit)
      word_nums.append(d[first_word_num] + '-' + d[n[1]])
    else:
      word_nums.append(d[n])
  print (' '.join(word_nums))
