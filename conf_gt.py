from conf import Conf
import logger
import os

class ConfGetTrain(Conf):
    def __init__(self, usage):
        self.width = 10
        self.height = 10
        self.ts_intv = 0.001
        self.lba_max = 0
        self.path_out = None
        self.n_forwards = 1
        self.no_csv = False
        super().__init__('o:d:i:M:f:H', usage)

    def handleOpt(self, o, a):
        if o == '-o':
            self.path_out = a
        elif o == '-d':
            self.__parse_bmp_dim(a)
        elif o == '-i':
            self.ts_intv = float(a)
        elif o == '-M':
            self.lbamax = int(a)
        elif o == '-f':
            self.n_forwards = int(a)
        elif o == '-H':
            self.no_csv = True

    def __parse_bmp_dim(self, dim):
        if 'x' in dim:
            width, height = dim.split(sep='x', maxsplit=1)
            self.width = int(width)
            self.height = int(height)

    def check(self):
        if len(self.paths) == 0:
            logger.error("empty path")
            exit(1)
        for path in self.paths:
            if not os.path.exists(path):
                logger.error("input file does not exist: {}".format(path))
                exit(1)
        if not self.path_out is None:
            if os.path.exists(self.path_out):
                logger.error("output file exists: {}".format(self.path_out))
                exit(1)
