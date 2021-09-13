#!/usr/bin/env python3

def swap_keys_values(dict):
  new_dict = {value: key for key, value in dict.items()}
  return new_dict
