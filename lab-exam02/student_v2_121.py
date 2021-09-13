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


def main():

    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)
    print(s1.get_mark('CA103'))

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)
    print(s2.get_mark('CA117'))

if __name__ == '__main__':
    main()
