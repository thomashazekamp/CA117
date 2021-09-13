#!/usr/bin/env python3

class Queue(object):

  def __init__(self):
    self.list = []

  def enqueue(self, new):
    self.list.append(new)

  def dequeue(self):
    return self.list.pop(0)

  def first(self):
    return self.list[0]

  def is_empty(self):
    return len(self.list) == 0

  def __len__(self):
    return len(self.list)


def main():

    q = Queue()

    print(len(q))
    q.enqueue(1)
    print(q.first())
    print(q.is_empty())
    print(q.dequeue())
    print(q.is_empty())
    try:
        print(q.dequeue())
    except IndexError:
        print('Error')
    try:
        print(q.first())
    except IndexError:
        print('Error')
    q.enqueue('cat')
    q.enqueue('dog')
    q.enqueue('fish')
    print(len(q))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())

if __name__ == '__main__':
    main()
