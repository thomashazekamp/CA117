#!/usr/bin/env python3

import sys

dict_d = {}
dict_n = {}

def calc(line):
  line.pop(0)
  line.pop(-1)
  for index, word in enumerate(line):
    if word in dict_d:
      line[index] = dict_d[word]
    elif word not in dict_d and word != '-' and word != '+':
      return 'unknown'
      break
  return eval(''.join(line))

for line in sys.stdin:
  line = line.strip()
  split_l = line.split()
  definition = split_l[0]

  if definition == 'def':
    if split_l[1] in dict_d:
      for key, value in dict(dict_n).items():
        if value == split_l[1]:
          del dict_n[key]
    dict_d[split_l[1]] = split_l[2]
    dict_n[int(split_l[2])] = split_l[1]
    #print ('this is a definition')

  if definition == 'calc':
    #print ('this is going to calculate')
    original_line = line.split()
    original_line.pop(0)
    original_line = ' '.join(original_line)
    return_v = calc(split_l)
    if return_v == 'unknown':
      print (original_line + ' unknown')
    else:
      if return_v in dict_n:
        print (original_line + ' ' + dict_n[return_v])
      else:
        print (original_line + ' unknown')

  if definition == 'clear':
    #print ('this is going to clear all definitions in dictonary')
    dict_d.clear()
    dict_n.clear()

#print (dict_d)
#print (dict_n)
# replace the defenitions with corrisponding dict keys then eval() them and get answer
