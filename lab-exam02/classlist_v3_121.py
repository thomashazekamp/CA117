#!/usr/bin/env python3

class Student(object):

  def __init__(self, name, address, sid):
    self.name = name
    self.address = address
    self.sid = sid
    self.dict = {}

  def __str__(self):
    l = []
    l.append(f'Name: {self.name}')
    l.append(f'Address: {self.address}')
    l.append(f'ID: {self.sid}')
    return '\n'.join(l)

  def add_mark(self, module, mark):
    self.dict[module] = mark

  def get_mark(self, module):
    if module in self.dict:
      return self.dict[module]
    else:
      return f'Not registered for module'

def sort_on(s):
  return s[1]

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

  def least_popular_module(self):
    self.mod_d = {}
    for s in self.d.values():
      for key in s.dict.keys():
        if key not in self.mod_d:
          self.mod_d[key] = 1
        else:
          self.mod_d[key] += 1
    return min(self.mod_d.items(), key=sort_on)[0]
    #  return f'CA172'
    #  for key in self.d:
    #  print (self.d[key])


def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)
    s3 = Student('Mikhail Tal', 'Belfast', 17884786)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)

    s3.add_mark('CA103', 80)
    s3.add_mark('CA106', 90)

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl.least_popular_module())

if __name__ == '__main__':
    main()
