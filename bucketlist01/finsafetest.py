#!/usr/bin/env python3

import sys

dict_d = {}  # this is the dict with all definitions as keys and their respective numbers as values
dict_n = {}  # this is the dict with the numbers as keys and definitions as values

def calc(line):  # this function calculates the output of the calc, into a integer or unknown if the definition is not part of dict_defs
  line.pop(0)
  line.pop(-1)
  for index, word in enumerate(line):  # replacing the definitions with its values
    if word in dict_d:
      line[index] = dict_d[word]
    elif word not in dict_d and word != '-' and word != '+':
      return 'unknown'
      break
  return eval(''.join(line))  # this evaluates the string as an expression

for line in sys.stdin:
  line = line.strip()
  split_line = line.split()
  definition = split_line[0]

  if definition == 'def':
    if split_line[1] in dict_d:
      for key, value in dict(dict_n).items():
        if value == split_line[1]:
          del dict_n[key]  # deletes any previous definitions
    dict_d[split_line[1]] = split_line[2]
    dict_n[int(split_line[2])] = split_line[1]

  if definition == 'calc':
    original_line = line.split()
    original_line.pop(0)
    original_line = ' '.join(original_line)
    return_value = calc(split_line)
    if return_value == 'unknown':
      print (original_line + ' unknown')
    else:
      if return_value in dict_n:
        print (original_line + ' ' + dict_n[return_value])
      else:
        print (original_line + ' unknown')

  if definition == 'clear':
    dict_defs.clear()
    dict_nums.clear()
