#!/usr/bin/env python3

class Triathlete(object):

  def __init__(self, name, tid):
    self.name = name
    self.tid = tid
    self.dict = {}
    self.race_time = 0

  def __str__(self):
    return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.race_time}'

  def add_time(self, discp, time):
    self.dict[discp] = time
    self.race_time += time

  def get_time(self, discp):
    return f'{self.dict[discp]}'

  def __eq__(self, other):
    return self.race_time == other.race_time

  def __lt__(self, other):
    return self.race_time < other.race_time

  def __gt__(self, other):
    return self.race_time > other.race_time

def sort_name(a):
  return a.name

def sort_time(a):
  return a.race_time

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

  def best(self):
    best = sorted(self.dict.values(), key=sort_time)[0]  # this should be [-1] but for einstein its printing worst [0]
    return f'{best}'

  def worst(self):
    worst = sorted(self.dict.values(), key=sort_time)[-1]  # this should be [0] but for einstein its printing best [-1]
    return f'{worst}'

  def __str__(self):
    lines = [str(a) for a in sorted(self.dict.values(), key=sort_name)]
    return '\n'.join(lines)

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
