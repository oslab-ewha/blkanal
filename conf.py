import sys
import getopt
import logger

readonly = False
writeonly = False
pidonly = []
n_lookbacks = 1
lba_start = 0
lba_end = -1
lba_max = 0
ts_start = 0
ts_end = 10000000
path = None
grid_nx = 5
grid_ny = 10
ts_unit = 0.005
lba_start_from_1 = False

class Conf:
    def __init__(self, optspec, usage):
        self.usage = usage
        self.__parseArgs("hRWP:b:B:M:T:G:u:z" + optspec)

    def __parseArgs(self, optspec):
        global  readonly, writeonly, pidonly, n_lookbacks, lba_max, path, paths, ts_unit, lba_start_from_1

        try:
            opts, args = getopt.getopt(sys.argv[1:], optspec)
        except getopt.GetoptError:
            logger.error("invalid option")
            self.usage()
            exit(1)

        for o, a in opts:
            if o == '-h':
                self.usage()
                exit(0)
            if o == '-R':
                readonly = True
            elif o == '-W':
                writeonly = True
            elif o == '-P':
                self.__parse_pid_only(a)
            elif o == '-b':
                n_lookbacks = int(a)
            elif o == '-B':
                self.__parse_lba_range(a)
            elif o == '-M':
                lba_max = int(a)
            elif o == '-T':
                self.__parse_ts_range(a)
            elif o == '-G':
                self.__parse_grid_dim(a)
            elif o == '-u':
                ts_unit = float(a)
            elif o == '-z':
                lba_start_from_1 = True
            else:
                self.handleOpt(o, a)
        if len(args) < 1:
            return False

        if len(args) == 1:
            path = args[0]
            paths = [ args[0] ]
        else:
            paths = args

        self.check()
        return True

    def __parse_lba_range(self, range):
        global  lba_start, lba_end

        if not '-' in range:
            lba_start = int(range)
        else:
            start, end = range.split(sep='-', maxsplit=1)
            lba_start = int(start)
            lba_end = int(end)

    def __parse_ts_range(self, range):
        global      ts_start, ts_end

        if not '-' in range:
            ts_start = float(range)
        else:
            start, end = range.split(sep='-', maxsplit=1)
            ts_start = float(start)
            ts_end = float(end)

    def __parse_grid_dim(self, dim):
        if 'x' in dim:
            global      grid_nx, grid_ny

            nx, ny = dim.split(sep='x', maxsplit=1)
            grid_nx = int(nx)
            grid_ny = int(ny)

    def __parse_pid_only(self, pidset):
        global  pidonly

        pidonly = []
        for p in pidset.split(sep=','):
            pidonly.append(int(p))

    def handleOpt(self, o, a):
        pass

    def check(self):
        pass
