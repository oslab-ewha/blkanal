#!/usr/bin/python3

import sys
import logger
import trace_access
import plot
from conf_ba import ConfBlkAnal

def __usage_BlkAnalysis():
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
    def analyze(self, conf):
        ta = trace_access.TraceAccess(conf)
        if not ta.load(conf.path):
            return
        if conf.plotting_mode:
            plot.plot(ta, conf)
        else:
            ta.summary()

if __name__ == "__main__":
    import blkanal

    logger.init("blkanal")

    ba = blkanal.BlkAnalysis()

    exit(ba.analyze(ConfBlkAnal(__usage_BlkAnalysis)))
