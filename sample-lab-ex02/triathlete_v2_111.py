#!/usr/bin/env python3

class Triathlete(object):

  def __init__(self, name, tid):
    self.name = name
    self.tid = tid
    self.dict = {}
    self.race_time = 0

  def __str__(self):
    return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.race_time}'

  def add_time(self, discp, time):
    self.dict[discp] = time
    self.race_time += time

  def get_time(self, discp):
    return f'{self.dict[discp]}'

def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()
