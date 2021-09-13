#!/usr/bin/env python3

'''Demonstrate mapping from list to dictionary.'''

import sys

from l2d_041 import l2d

def main():
    d = l2d(sys.stdin)
    for k, v in sorted(d.items()):
        print (f'{k} : {v}')

if __name__ == '__main__':
    main()
