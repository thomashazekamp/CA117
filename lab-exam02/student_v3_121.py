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
    l.append(f'Average mark: {self.avg_mark():.2f}')
    return '\n'.join(l)

  def add_mark(self, module, mark):
    self.dict[module] = mark

  def get_mark(self, module):
    if module in self.dict:
      return self.dict[module]
    else:
      return f'Not registered for module'

  def avg_mark(self):
    if not self.dict:
      return 0
    else:
      return (sum([m for m in self.dict.values()])) / len(self.dict.keys())

def main():

    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)
    s3 = Student('Mikhail Tal', 'Belfast', 17884786)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)
    print(s1)

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)
    print(s2)

    print(s3)

if __name__ == '__main__':
    main()
