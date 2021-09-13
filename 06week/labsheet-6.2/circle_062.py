#!/usr/bin/env python3

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
  tot_dis = r1 + r2
  p_dis = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)
  return p_dis < tot_dis

def main():
  pass
  # print (overlap())
  # print (overlap(10))
  # print (overlap(10,10))
  # print (overlap(10,10,10))
  # print (overlap(10,0,10))
  # print (overlap(10,0,1,8,0,1))
  # print (overlap(10,0,1,8,0,2))

if __name__ == '__main__':
  main()
