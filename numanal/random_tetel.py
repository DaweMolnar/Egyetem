#!/usr/bin/python
import random
import sys, getopt
def main(argv):
    inputfile = ''
    numtimes = 0
    try:
        opts, args = getopt.getopt(argv,"hi:n:",["ifile=","num="])
    except getopt.GetoptError:
      print 'random_tetel.py -i <inputfile>'
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'random_tetel.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-n", "--num"):
            numtimes = int(arg)
    for x in xrange(numtimes):
        line = random.choice(open(inputfile).readlines())
        print line

if __name__ == "__main__":
       main(sys.argv[1:])
