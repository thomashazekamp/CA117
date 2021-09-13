#!/usr/bin/env python3

import sys

low = []
for word in sys.stdin:
  word = word.strip()
  low.append(word)

def vowels_in(s):  # function to get word with all aeiou
  return 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s

count = 0
for word in low:
  if word.count('e') > count:
    count = word.count('e')

all_vowels = [word for word in low if vowels_in(word.lower())]  # all words with all 5 vowels
short_av = min(all_vowels, key=len)  # the shortest word in the list
print (f'Shortest word containing all vowels: {short_av}')

iary_words = [word for word in low if word.lower().endswith('iary')]  # all words that end with 'iary'
num_iw = len(iary_words)  # the number of words in the list
print (f'Words ending in iary: {num_iw}')

most_es = [word for word in low if word.count('e') == count]  # list of most e words
print (f'Words with most e\'s: {str(most_es)}')
