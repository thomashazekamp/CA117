#!/usr/bin/env python3

def power(a, b):
  if b == 0:
    return 1
  return a * power(a, b - 1)

def main():
    print(power(2, 3))
    print(power(4, 4))
    print(power(2, 32))
    print(power(10, 3))
    print(power(8, 0))

if __name__ == '__main__':
    main()
