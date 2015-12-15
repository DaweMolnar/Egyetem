#!/usr/bin/python
import random
import sys, getopt
def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print 'random_tetel.py -i <inputfile>'
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'random_tetel.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    line = random.choice(open(inputfile).readlines())
    print line

if __name__ == "__main__":
       main(sys.argv[1:])
