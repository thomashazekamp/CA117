#!/usr/bin/env python3

def build_dictionary(stream):
  dict = {}
  for line in stream:
    [word, num] = line.strip().split()
    dict[word] = num
  return dict

def extract_range(d, low, high):
  nd = {}
  for k, v in d.items():
    if int(v) >= low and int(v) <= high:
      nd[k] = v
  return nd
