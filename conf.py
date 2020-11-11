import sys
import getopt
import logger

class Conf:
    def __init__(self, optspec, usage):
        self.usage = usage
        self.readonly = False
        self.writeonly = False
        self.pidonly = []
        self.n_lookbacks = 1
        self.lba_start = 0
        self.lba_end = -1
        self.ts_start = 0
        self.ts_end = 10000000
        self.path = None

        self.__parseArgs("hRWP:b:B:T:" + optspec)

    def __parseArgs(self, optspec):
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
                self.readonly = True
            elif o == '-W':
                self.writeonly = True
            elif o == '-P':
                self.pidonly = self.__parse_pid_only(a)
            elif o == '-b':
                self.n_lookbacks = int(a)
            elif o == '-B':
                self.__parse_lba_range(a)
            elif o == '-T':
                self.__parse_ts_range(a)
            else:
                self.handleOpt(o, a)
        if len(args) < 1:
            return False

        if len(args) == 1:
            self.path = args[0]
            self.paths = [ args[0] ]
        else:
            self.paths = args

        self.check()
        return True

    def __parse_lba_range(self, range):
        if not '-' in range:
            self.lba_start = int(range)
        else:
            start, end = range.split(sep='-', maxsplit=1)
            self.lba_start = int(start)
            self.lba_end = int(end)

    def __parse_ts_range(self, range):
        if not '-' in range:
            self.ts_start = float(range)
        else:
            start, end = range.split(sep='-', maxsplit=1)
            self.ts_start = float(start)
            self.ts_end = float(end)

    def __parse_pid_only(self, pidset):
        pids = []
        for p in pidset.split(sep=','):
            pids.append(int(p))
        return pids

    def handleOpt(self, o, a):
        pass

    def check(self):
        pass
