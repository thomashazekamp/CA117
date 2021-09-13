#!/usr/bin/env python3

date = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2}\b'
phone = r'\b01[\s-]\d{7}\b'
email = r'\b(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*\b'
ldate = r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2,4}'

def main():
  print (len(date))
  print (len(phone))
  print (len(email))
  print (len(ldate))

if __name__ == '__main__':
  main()
