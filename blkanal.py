#!/usr/bin/python3

import sys
import logger
import trace_access
import plot
import conf
from conf_ba import ConfBlkAnal

def __usage_BlkAnalysis():
    print("""\
Usage: blkanal.py [<options>] <path>
  <options>
   -p: plotting mode
   -G <dim>: scatter grid dimension
   -D: display lba difference
   -B <block range>
   -z: adjust lba start from 1
   -T <timestamp range>
   -b <cnt>: look back count for previous access
   -R: analyze only read access
   -W: analyze only write access
   -P <pid>: analyze accesses with given pid
""")

class BlkAnalysis:
    def analyze(self):
        ta = trace_access.TraceAccess()
        if not ta.load(conf.path):
            return
        if conf.plotting_mode:
            plot.plot(ta)
        else:
            ta.summary()

if __name__ == "__main__":
    import blkanal

    logger.init("blkanal")

    ba = blkanal.BlkAnalysis()
    ConfBlkAnal(__usage_BlkAnalysis)
    exit(ba.analyze())
