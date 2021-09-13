#!/usr/bin/env python3

def swap_unique_keys_values(dict):
  new_dict = {value: key for key, value in dict.items() if (list(dict.values())).count(value) < 2}
  return new_dict
