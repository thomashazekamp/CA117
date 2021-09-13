#!/usr/bin/env python3

# --> Stack class

class Stack(object):

  def __init__(self):
    self.list = []

  def push(self, e):
    self.list.append(e)

  def pop(self):
    return self.list.pop()

  def top(self):
    return self.list[-1]

  def is_empty(self):
    return len(self.list) == 0

  def __len__(self):
    return len(self.list)

# --> Function matcher

def matcher(line):

  d = {')': '(', ']': '[', '}': '{'}
  s = Stack()

  for c in line:
    if c in d.values():
      s.push(c)

    if c in d.keys():
      try:
        if d[c] != s.pop():
          return False
      except IndexError:
        return False

  return s.is_empty()

import sys

def main():

  for line in sys.stdin:
    print(matcher(line.strip()))

if __name__ == '__main__':
  main()
