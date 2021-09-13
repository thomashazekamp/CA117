#!/usr/bin/env python3

import sys

#for diamond_size in sys.stdin:
#  diamond_size = int(diamond_size.strip())
#  print ((diamond_size - 1) * " ", "*", (diamond_size - 1) * " ")
#  print ((diamond_size - 2) * " ", "* *", (diamond_size - 2) * " ")
#  print ((diamond_size - 3) * " ", "* * *", (diamond_size - 3) * " ")
#  print ((diamond_size - 4) * " ", "* * * *", (diamond_size - 4) * " ")
#  print ((diamond_size - 5) * " ", "* * * * *", (diamond_size - 5) * " ")
#  print ((diamond_size - 4) * " ", "* * * *", (diamond_size - 4) * " ")
#  print ((diamond_size - 3) * " ", "* * *", (diamond_size - 3) * " ")
#  print ((diamond_size - 2) * " ", "* *", (diamond_size - 2) * " ")
#  print ((diamond_size - 1) * " ", "*", (diamond_size - 1) * " ")

for diamond_size in sys.stdin:
  diamond_size = int(diamond_size.strip())
#  print (f"{'*':^{diamond_size}s}")
#for diamond_size in sys.stdin:
#  diamond_size = int(diamond_size.strip())
#  for i in range(1, diamond_size + 1):
#    print ((diamond_size - i) * " " + (i * "* ") + (diamond_size - i) * " ")
#  for j in range(diamond_size - 1, 0, -1):
#    print ((diamond_size - j) * " " + (j * "* ") + (diamond_size - j) * " ")
  i = 1
  while i < (diamond_size + 1):
    print (((diamond_size - i) * " " + (i * "* ")).rstrip())
    i = i + 1
  j = diamond_size - 1
  while j > 0:
    print (((diamond_size - j) * " " + (j * "* ")).rstrip())
    j = j - 1
