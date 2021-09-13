#!/usr/bin/env python3

class Student(object):

  def __init__(self, surname, forename, sid, modlist=None):
    self.sid = sid
    self.surname = surname
    self.forename = forename
    self.modlist = modlist

  def add_module(self, add_mod):
    if self.modlist is None:
      self.modlist = []
    (self.modlist).append(add_mod)

  def del_module(self, del_mod):
    if del_mod in self.modlist:
      (self.modlist).remove(del_mod)

  def print_details(self):
    print (f'ID: {self.sid}')
    print (f'Surname: {self.surname}')
    print (f'Forename: {self.forename}')
    print (f"Modules: {' '.join(self.modlist)}")

def main():

    student1 = Student('Murphy', 'Jimmy', 15234654)
    student1.add_module('CA117')
    student1.add_module('CA116')
    student1.add_module('CA114')
    student1.print_details()

    student2 = Student('Lannister', 'Cersei', 15876123, ['CA115', 'CA216'])
    student2.del_module('CA216')
    student2.del_module('CA117')
    student2.del_module('CA216')
    student2.add_module('CA117')
    student2.print_details()

if __name__ == '__main__':
    main()
