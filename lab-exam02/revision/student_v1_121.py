#!/usr/bin/env python3

class Student(object):

  def __init__(self, name, address, sid):
    self.name = name
    self.address = address
    self.sid = sid
    self.dict = {}

  def add_mark(self, module, score):
    self.dict[module] = score

  def get_mark(self, module):
    if module in self.dict:
      return self.dict[module]
    return f'Not registered for module'

  def avg_mark(self):
    if not self.dict:
      return 0
    return sum(self.dict.values())/len(self.dict.values())

  def __eq__(self, other):
    return self.avg_mark() == other.avg_mark()

  def __lt__(self, other):
    return self.avg_mark() < other.avg_mark()

  def __gt__(self, other):
    return self.avg_mark() > other.avg_mark()

  def __str__(self):
    lines = []
    lines.append(f'Name: {self.name}')
    lines.append(f'Address: {self.address}')
    lines.append(f'Average mark: {self.avg_mark():.2f}')
    return '\n'.join(lines)

def sort_on(s):
  return s[1]

class Classlist(object):

  def __init__(self):
    self.map = {}

  def add(self, s):
    self.map[s.sid] = s

  def remove(self, sid):
    if sid in self.map:
      del self.map[sid]

  def lookup(self, sid):
    if sid in self.map:
      return self.map[sid]
    else:
      return None

  def __str__(self):
    lines = [f'{self.map[key]}'for key in sorted(self.map)]
    return '\n'.join(lines)

  def least_popular_module(self):
    self.mod_d = {}
    for key, value in self.map.items():
      for m in value.dict.keys():
        if m not in self.mod_d:
          self.mod_d[m] = 1
        else:
          self.mod_d[m] += 1
    return min(self.mod_d.items(), key=sort_on)[0]

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
