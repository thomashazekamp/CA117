#!/usr/bin/env python3

class Contact(object):

  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email

  def __str__(self):
    return f'{self.name} {self.phone} {self.email}'

class ContactList(object):

  def __init__(self, d=None):
    if d is None:
      d = {}
    self.dict = d

  def add_contact(self, c):
    self.dict[c.name] = c

  def del_contact(self, c):
    if c in self.dict:
      del self.dict[c]

  def get_contact(self, c):
    if c in self.dict:
      return self.dict[c]
    else:
      return None

  def __str__(self):
    lines = [str(self.dict[key]) for key in sorted(self.dict)]
    return 'Contact list\n' + '------------\n' + '\n'.join(lines)


import sys

def main():
  cl = ContactList()
  for line in sys.stdin:
      [name, phone, email] = line.strip().split()
      c = Contact(name, phone, email)
      cl.add_contact(c)

  c = cl.get_contact('Jimmy')
  print (c)
  c = cl.get_contact('Mary')
  print (c)

  print (cl)
  cl.del_contact('Maggie')
  cl.del_contact('Maggie')

  c = Contact('Sue', '087-6442378', 'sue@eircom.net')
  cl.add_contact(c)
  c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
  cl.add_contact(c)
  print (cl)

if __name__ == '__main__':
  main()
