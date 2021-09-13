#!/usr/bin/env python3

import sys

def procfile(filename):
  try:
    with open(filename, 'r') as f:
      best_mark = -1  # initial best mark
      best_student = ""  # a string of the best students
      for line in f:
        try:
          mark, name = line.strip().split(maxsplit=1)  # multiple assignments like having mark = ... and name = ....
          mark = int(mark)

          if mark == best_mark:
            best_student = best_student + ", " + name
          elif mark > best_mark:
            best_student = name
            best_mark = mark

        except ValueError:
          print (f"Invalid mark {mark} encountered. Skipping.")

    print (f'Best student(s): {best_student}')
    print (f'Best mark: {best_mark}')

  except FileNotFoundError:
    print (f'The file {filename} could not be opened.')

procfile(sys.argv[1])
