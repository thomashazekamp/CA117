#!/usr/bin/env python3

import sys

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

  def __str__(self):
    return str(self.list[0])

# --> Dictionaries for operators

def addition(a, b):
  return a + b

def subtraction(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  return a / b

def negative(a):
  return a * -1

def root(a):
  return a ** 0.5

# --> calculator Function

def calculator(line):

  line = line.split(' ')
  i = 0
  while i < len(line):
    try:
      if line[i].isdigit() or float(line[i]):
        line[i] = float(line[i])
      i = i + 1
    except ValueError:
      pass
      i = i + 1
  #print (line)

  s = Stack()
  d1 = {'+': addition, '-': subtraction, '*': multiplication, '/': division}
  d2 = {'n': negative, 'r': root}
  for v in line:
    try:
      if isinstance(v, float):
        s.push(v)
    except ValueError:
      pass
    if isinstance(v, str) and v in d1.keys() or v in d2.keys():
       if v in d1.keys():
         b = s.pop()
         a = s.pop()
         s.push(d1[v](a, b))
       else:
         a = s.pop()
         s.push(d2[v](a))
  final = str(s)
  return float(final)

#def main():
#  for line in sys.stdin:
#    try:
#      a = calculator(line.strip())
#      print (a)
#    except IndexError:
#      print ('test')

def main():

  for line in sys.stdin:
    try:
      a = calculator(line.strip())
      print ('{:.2f}'.format(a))
    except IndexError:
      print ('Invalid RPN expression')

if __name__ == '__main__':
  main()
