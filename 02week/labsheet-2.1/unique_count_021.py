#!/usr/bin/env python3

import sys
import string

tokens = sys.stdin.read().split()
unique = []
for token in tokens:
  token = token.lower()
  for c in token:
    if c in string.punctuation:
      token = token.replace(c, "")
  if token.isalnum() is True and token not in unique:
    unique.append(token)
print (len(unique))
