import conf
import logger
import os

class ConfGetTrain(conf.Conf):
    def __init__(self, usage):
        conf.path_out = None
        conf.n_forwards = 1
        conf.no_csv = False
        super().__init__('o:f:H', usage)

    def handleOpt(self, o, a):
        if o == '-o':
            conf.path_out = a
        elif o == '-f':
            conf.n_forwards = int(a)
        elif o == '-H':
            conf.no_csv = True

    def check(self):
        if len(conf.paths) == 0:
            logger.error("empty path")
            exit(1)
        for path in conf.paths:
            if not os.path.exists(path):
                logger.error("input file does not exist: {}".format(path))
                exit(1)
        if not conf.path_out is None:
            if os.path.exists(conf.path_out):
                logger.error("output file exists: {}".format(conf.path_out))
                exit(1)
