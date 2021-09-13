#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()
all = []
for line in input:
  words = line.split()
  if words[2].isalpha() is True:
    words[1] = " ".join(words[1:3])
    words.pop(2)
    if words[2].isalpha() is True:
      words[1] = " ".join(words[1:3])
      words.pop(2)
  all.append(words)

i = 1
long_team = all[0][1]
while i < len(all):
  if len(all[i][1]) > len(long_team):
    long_team = all[i][1]
  i = i + 1

long_team = len(long_team)
# print (long_team)
h1 = "POS"
h2 = "CLUB"
h3 = "P"
h4 = "W"
h5 = "D"
h6 = "L"
h7 = "GF"
h8 = "GA"
h9 = "GD"
h10 = "PTS"
print (f"{h1:<s} {h2:<{long_team}s} {h3:>2s} {h4:>3s} {h5:>3s} {h6:>3s} {h7:>3s} {h8:>3s} {h9:>3s} {h10:>3s}")

for line in input:
  words = line.split()
  if words[2].isalpha() is True:
    words[1] = " ".join(words[1:3])
    words.pop(2)
    if words[2].isalpha() is True:
      words[1] = " ".join(words[1:3])
      words.pop(2)
  print (f"{words[0]:>3s} {words[1]:<{long_team}s} {words[2]:>2s} {words[3]:>3s} {words[4]:>3s} {words[5]:>3s} {words[6]:>3s} {words[7]:>3s} {words[8]:>3s} {words[9]:>3s}")
