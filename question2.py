#!/usr/bin/python

import sys

def is_num(word):
    try: 
        float(word)
        return True
    except ValueError:
       pass

if __name__ == "__main__":
    word = sys.argv[1]
    if is_num(word):
        print "Number"
    else:
        print "String"
