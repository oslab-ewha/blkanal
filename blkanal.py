#!/usr/bin/python3

import sys
import logger
import trace_access
import plot
import args

def usage():
    print("""\
Usage: blkanal.py [<options>] <path>
  <options>
   -R: analyze only read access
   -W: analyze only write access
""")

class BlkAnalysis:
    def analyze(self, args):
        global  readonly, writeonly
        ta = trace_access.TraceAccess()
        if not ta.load(args.path):
            return
        plot.plot(ta, args)

if __name__ == "__main__":
    import blkanal

    logger.init("blkanal")

    if not args.parseArgs():
        usage()
        exit(1)

    ba = blkanal.BlkAnalysis()
    exit(ba.analyze(args))
