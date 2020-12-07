import sys
import getopt
import logger

readonly = False
writeonly = False
pidonly = []
n_lookbacks = 1
lba_start = 0
lba_end = -1
ts_start = 0
ts_end = 10000000
path = None
lba_start_from_1 = False

class Conf:
    def __init__(self, optspec, usage):
        self.usage = usage
        self.__parseArgs("hRWP:b:B:T:z" + optspec)

    def __parseArgs(self, optspec):
        global  readonly, writeonly, pidonly, n_lookbacks, path, paths, lba_start_from_1

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
            elif o == '-T':
                self.__parse_ts_range(a)
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

    def __parse_pid_only(self, pidset):
        global  pidonly

        pidonly = []
        for p in pidset.split(sep=','):
            pidonly.append(int(p))

    def handleOpt(self, o, a):
        pass

    def check(self):
        pass
