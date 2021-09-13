#!/usr/bin/env python3

def fibonacci(n):
  if n == 0 or n == 1:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(5))
    print(fibonacci(8))

if __name__ == '__main__':
    main()
