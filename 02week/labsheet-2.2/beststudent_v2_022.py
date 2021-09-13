#!/usr/bin/env python3

import sys

def procfile(filename):
  try:
    with open(filename, 'r') as f:
      best_mark = -1
      best_student = ""
      for line in f:
        mark, name = line.strip().split(maxsplit=1)
        mark = int(mark)

        if mark > best_mark:
          best_mark, best_student = mark, name

    print (f'Best student: {best_student}')
    print (f'Best mark: {best_mark}')

  except ValueError:
    print (f"Invalid mark {mark} encountered. Exiting.")

  except FileNotFoundError:
    print (f'The file {filename} could not be opened.')

procfile(sys.argv[1])
