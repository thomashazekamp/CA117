#!/usr/bin/env python3

import sys

phone_book = {}

filename = sys.argv[1]
with open(filename, 'r') as f:
  for line in f:
    line = line.strip().split()
    phone_book[line[0]] = [line[1], line[2]]

def contacts(name):
  if name in phone_book:
    print (f'Phone: {phone_book[name][0]}')
    return f'Email: {phone_book[name][1]}'
  else:
    return 'No such contact'

for line in sys.stdin:
  line = line.rstrip()
  print (f'Name: {line}')
  print (contacts(line))
