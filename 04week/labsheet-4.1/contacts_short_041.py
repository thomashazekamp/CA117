#!/usr/bin/env python3

import sys

phone_book = {}

filename = sys.argv[1]
with open(filename, 'r') as f:
  for line in f:
    line = line.strip().split()
    phone_book[line[0]] = line[1]

def contacts(name):
  if name in phone_book:
    return f'Phone: {phone_book[name]}'
  else:
    return 'No such contact'

for line in sys.stdin:
  line = line.rstrip()
  print (f'Name: {line}')
  print (contacts(line))
