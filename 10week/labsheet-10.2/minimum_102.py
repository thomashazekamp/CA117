#!/usr/bin/env python3

def minimum(list):

  def partition(a, p, r):
    q = j = p
    while j < r:
      if a[j] <= a[r]:
        a[q], a[j] = a[j], a[q]
        q = q + 1
      j = j + 1
    a[q], a[r] = a[r], a[q]
    return q

  def quicksort(a, p, r):
    if r <= p:
      return
    q = partition(a, p, r)
    quicksort(a, p, q - 1)
    quicksort(a, q + 1, r)

  quicksort(list, 0, len(list) - 1)
  return list[0]

def main():
    min = None
    print(minimum([6, 5, 1, 3, 4]))
    print(minimum([6, 5, 11, 3, 4]))
    print(minimum([6, 15, 11, 13, 14]))
    print(minimum([6, 15, 11, 13, 4]))

if __name__ == '__main__':
    main()
