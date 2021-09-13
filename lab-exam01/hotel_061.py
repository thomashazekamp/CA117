#!/usr/bin/env python3

import sys

def main():
  try:
    nums = sys.stdin.readline().strip()
    tokens = nums.split()
    max_n, rooms = tokens[0], tokens[1:]
    free_room = []
    for i in range(1, int(max_n) + 1):
      if str(i) not in rooms:
        free_room.append(i)
    print (min(free_room))
  except ValueError:
    print ('no room')

if __name__ == '__main__':
  main()
