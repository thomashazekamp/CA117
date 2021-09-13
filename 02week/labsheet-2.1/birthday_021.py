#!/usr/bin/env python3

import sys
import calendar

day_zero = "Monday's child is fair of face."
day_one = "Tuesday's child is full of grace."
day_two = "Wednesday's child is full of woe."
day_three = "Thursday's child has far to go."
day_four = "Friday's child is loving and giving."
day_five = "Saturday's child works hard for a living."
day_six = "Sunday's child is fair and wise and good in every way."
born = "You were born on a"

def week_day():
  if num_day == 0:
    return f"{born} Monday and {day_zero}"
  elif num_day == 1:
    return f"{born} Tuesday and {day_one}"
  elif num_day == 2:
    return f"{born} Wednesday and {day_two}"
  elif num_day == 3:
    return f"{born} Thursday and {day_three}"
  elif num_day == 4:
    return f"{born} Friday and {day_four}"
  elif num_day == 5:
    return f"{born} Saturday and {day_five}"
  else:
    return f"{born} Sunday and {day_six}"

for date in sys.stdin:
  date = date.strip().split()
  num_day = calendar.weekday(int(date[2]), int(date[1]), int(date[0]))
  print (week_day())
