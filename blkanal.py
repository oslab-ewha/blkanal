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
   -p: plotting mode
   -G <dim>: scatter grid dimension
   -D: display lba difference
   -B <block range>
   -T <timestamp range>
   -b <cnt>: look back count for previous access
   -R: analyze only read access
   -W: analyze only write access
   -P <pid>: analyze accesses with given pid
""")

class BlkAnalysis:
    def analyze(self, args):
        global  readonly, writeonly
        ta = trace_access.TraceAccess(args)
        if not ta.load(args.path):
            return
        if args.plotting_mode:
            plot.plot(ta, args)
        else:
            ta.summary()

if __name__ == "__main__":
    import blkanal

    logger.init("blkanal")

    if not args.parseArgs():
        usage()
        exit(1)

    ba = blkanal.BlkAnalysis()
    exit(ba.analyze(args))
