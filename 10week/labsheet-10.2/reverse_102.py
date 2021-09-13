#!/usr/bin/env python3

def reverse_list(list):
  if len(list) == 0:
    return []
  return [list.pop()] + reverse_list(list)  # adding two lists together recursively, *stack principle

def main():
    print(reverse_list([1, 2, 3]))
    print(reverse_list([3, 4, 5, 6]))
    print(reverse_list([1, 2]))

if __name__ == '__main__':
    main()
