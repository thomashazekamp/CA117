#!/usr/bin/env python3

import sys

# --> This program takes the total time taken to a traffic light and then gets the modulus of the lights cycle to check if there
#     is a wait time, then adds to the total time and keeps going for each traffic light.
# --> time_calc returns the total wait time if there is any. If prev_tot is 0, it means that this is the first traffic light.

def time_calc(pos, red, green, prev, prev_tot=0):
  cycle = red + green
  dis = pos - prev
  if prev_tot == 0:
    mod = pos % cycle
  else:
    mod = (prev_tot + dis) % cycle

  if 0 <= mod < red:  # Calculating the wait
    wait_time = red - mod
    tot_time = dis + wait_time
    return tot_time
  else:  # If there is no wait time it returns the time taken to travel to this traffic light
    return dis

def main():

  list = [line.strip() for line in sys.stdin]

  tot_time = 0
  road_dis = int(list[0])
  prev = 0
  prev_tot = 0
  i = 1
  while i < len(list):
    tlight = [int(n) for n in list[i].split()]
    pos, red, green = tlight[0], tlight[1], tlight[2]

    tot_time += time_calc(pos, red, green, prev, prev_tot)
    prev = pos  # prev is used to remember the distance from the previous traffic light to the next one in the while loop
    prev_tot = tot_time  # prev_tot is used to to have the total time taken from start to the curent traffic light
    i = i + 1

  remaining = road_dis - prev  # This is the leftover distance from the last traffic light to the end destination
  print (tot_time + remaining)

if __name__ == '__main__':
  main()
