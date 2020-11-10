#!/usr/bin/python3

import logger
import trace_train
from conf_gt import ConfGetTrain

def __usage_getrain():
    print("""\
Usage: getrain.py [<options>] <path>
  <options>
   -o <output>
   -d <dim>: bitmap dimension, format: widthxheight
   -i <interval>: timestamp interval for width
   -M <lba max>
   -B <block range>
   -T <timestamp range>
   -R: analyze only read access
   -W: analyze only write access
   -P <pid>: analyze accesses with given pid
   -H: human readable output(no csv)
""")

class GetTrain:
    def getdata(self, usage):
        conf = ConfGetTrain(usage)
        tt = trace_train.TraceTrain(conf)
        if not tt.load(conf.path):
            return
        tt.gen_train_data()

if __name__ == "__main__":
    import getrain

    logger.init("getrain")

    gt = getrain.GetTrain()
    exit(gt.getdata(__usage_getrain))
