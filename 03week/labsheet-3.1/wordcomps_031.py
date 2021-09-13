#!/usr/bin/env python3

import sys

words = []

def comps(words):
  stletters = [w for w in words if len(w) == 17]
  etletters = [w for w in words if len(w) >= 18]
  aletters = [w for w in words if w.lower().count("a") == 4]
  qletters = [w for w in words if w.lower().count("q") >= 2]
  cieletters = [w for w in words if "cie" in w]
  anagramwords = [w for w in words if w.lower().count("a") == 1 and w.lower().count("n") and w.lower().count("g") == 1 and w.lower().count("l") == 1 and w.lower().count("e") and len(w) == 5 and w != "angle"]
  print ("Words containing 17 letters: " + str(stletters))
  print ("Words containing 18+ letters: " + str(etletters))
  print ("Words with 4 a's: " + str(aletters))
  print ("Words with 2+ q's: " + str(qletters))
  print ("Words containing cie: " + str(cieletters))
  return ("Anagrams of angle: " + str(anagramwords))

for word in sys.stdin:
  word = word.strip()
  words.append(word)

print (comps(words))
