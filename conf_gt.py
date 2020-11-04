from conf import Conf

class ConfGetTrain(Conf):
    def __init__(self, usage):
        self.width = 10
        self.height = 10
        self.ts_intv = 0.001
        self.lba_max = 0
        self.path_out = None
        super().__init__('o:d:i:M:', usage)

    def handleOpt(self, o, a):
        if o == '-o':
            self.path_out = a
        elif o == '-d':
            self.__parse_bmp_dim(a)
        elif o == '-i':
            self.ts_intv = float(a)
        elif o == '-M':
            self.lbamax = int(a)

    def __parse_bmp_dim(self, dim):
        if 'x' in dim:
            width, height = dim.split(sep='x', maxsplit=1)
            self.width = int(width)
            self.height = int(height)
