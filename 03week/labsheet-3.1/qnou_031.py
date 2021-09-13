#!/usr/bin/env python3

import sys

all_words = []

def qnou(s):
  s = s.replace('qu', '--')
  return 'q' in s

low = sys.stdin.read().strip().split()
qnous = [word for word in low if qnou(word.lower())]
print (f'Words with q but no u: {str(qnous)}')
