#!/usr/bin/env python3

class Triathlete(object):

  def __init__(self, name, tid):
    self.name = name
    self.tid = tid

  def __str__(self):
    return f'Name: {self.name}\nID: {self.tid}'

def sort_name(a):
  return a.name

class Triathlon(object):

  def __init__(self, d=None):
    if d is None:
      d = {}
    self.dict = d

  def add(self, a):
    self.dict[a.tid] = a

  def remove(self, a):
    if a in self.dict:
      del self.dict[a]

  def lookup(self, a):
    if a in self.dict:
      return self.dict[a]
    return None

  def __str__(self):
    lines = [str(a) for a in sorted(self.dict.values(), key=sort_name)]
    return '\n'.join(lines)

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
