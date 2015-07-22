#!/usr/bin/env python

import sys, os, re
import json

def usage():
  return "./url.py '<url>'"

def match_keyword(url):

  regex = re.compile('(partner|alliance|customer)', flags=re.I)
  matches = regex.findall(url)

  return {'match_count': len(matches), 'matches': matches}

def main():
  if len(sys.argv) < 2:
    print usage()
    exit()  
    
  url = sys.argv[1]
  print json.dumps(match_keyword(url))

if __name__ == "__main__":
  main()
