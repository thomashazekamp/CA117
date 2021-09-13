#!/usr/bin/env python3

class Triathlete(object):

  def __init__(self, name, tid):
    self.name = name
    self.tid = tid

  def __str__(self):
    return f'Name: {self.name}\nID: {self.tid}'

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


def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)

if __name__ == '__main__':
    main()
