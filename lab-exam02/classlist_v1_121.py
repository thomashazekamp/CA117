#!/usr/bin/env python3

class Student(object):

  def __init__(self, name, address, sid):
    self.name = name
    self.address = address
    self.sid = sid

  def __str__(self):
    l = []
    l.append(f'Name: {self.name}')
    l.append(f'Address: {self.address}')
    l.append(f'ID: {self.sid}')
    return '\n'.join(l)

class Classlist(object):

  def __init__(self):
    self.d = {}

  def add(self, s):
    self.d[s.sid] = s

  def remove(self, s):
    if s in self.d:
      del self.d[s]

  def lookup(self, sid):
    if sid in self.d:
      return self.d[sid]
    else:
      return None

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)

    cl.add(s1)
    cl.add(s2)

    s = cl.lookup(17345654)
    assert(isinstance(s, Student))
    assert(s.name == 'Boris Spassky')
    assert(s.address == 'Dublin')
    assert(s.sid == 17345654)

    cl.remove(17345654)
    s = cl.lookup(17345654)
    assert(s is None)

if __name__ == '__main__':
    main()
