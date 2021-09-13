#!/usr/bin/env python3

def l2d(file):
  f = file.readlines()
  top = f[0].strip().split()
  bot = f[1].strip().split()
  dict = {}
  i = 0
  for t in top:
    while i < len(bot):
      dict[t] = int(bot[i])
      i = i + 1
      break
  return dict
