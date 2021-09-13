#!/usr/bin/env python3

class Point(object):

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return f'({self.x:.1f}, {self.y:.1f})'

  def midpoint(self, other):
    x = (self.x + other.x) / 2
    y = (self.y + other.y) / 2
    return Point(x, y)

class Circle(object):

  def __init__(self, c=None, r=0):
    if c is None:
      c = Point()
    self.radius = r
    self.centre = c

  def __str__(self):
    lines = []
    lines.append(f'Centre: {self.centre}')
    lines.append(f'Radius: {self.radius}')
    return '\n'.join(lines)

  def __add__(self, other):
    new_c = (self.centre).midpoint(other.centre)
    new_r = self.radius + other.radius
    return Circle(new_c, new_r)

def main():
  p1 = Point()
  p2 = Point(4, 6)
  c1 = Circle(p1, 10)
  c2 = Circle(p2, 5)
  c3 = c1 + c2
  print (c3)

  p3 = Point(10, 10)
  c4 = Circle(p3, 15)
  c5 = c2 + c4
  print (c5)

if __name__ == '__main__':
  main()
