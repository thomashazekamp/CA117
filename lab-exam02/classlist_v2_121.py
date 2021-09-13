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

  def __str__(self):
    lines = [f'{self.d[key]}'for key in sorted(self.d)]
    return '\n'.join(lines)

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)
    s3 = Student('Mikhail Tal', 'Belfast', 17884786)

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl)

if __name__ == '__main__':
    main()
