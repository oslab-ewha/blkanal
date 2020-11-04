import trace_data
import trace_context
import access

class TraceAccess(trace_data.TraceData):
    def __init__(self, conf):
        super().__init__()
        self.accesses = []
        self.n_reads = 0
        self.n_writes = 0
        self.contexts = {}
        self.lba_min = -1
        self.lba_max = 0
        self.__conf = conf

    def parseLine(self, row):
        acc = access.Access(row)
        if acc.lba < self.__conf.lba_start or (self.__conf.lba_end > 0 and acc.lba > self.__conf.lba_end):
            return
        if acc.ts < self.__conf.ts_start or acc.ts > self.__conf.ts_end:
            return
        if acc.is_read is None:
            return
        if self.__conf.pidonly >= 0:
            if self.__conf.pidonly != acc.pid:
                return

        if self.__conf.writeonly:
            if acc.is_read:
                return
        if self.__conf.readonly:
            if not acc.is_read:
                return
        if self.lba_min < 0 or acc.lba < self.lba_min:
            self.lba_min = acc.lba
        if acc.lba > self.lba_max:
            self.lba_max = acc.lba

        ctx = trace_context.TraceContext(row)
        if ctx in self.contexts:
            acc.context = self.contexts[ctx]
        else:
            self.contexts[ctx] = ctx
            acc.context = ctx

        acc.context.add(acc)
        acc.setLbaDiff(self.accesses[-1 * self.__conf.n_lookbacks:])
        self.accesses.append(acc)
        if acc.is_read:
            self.n_reads += 1
        else:
            self.n_writes += 1

    def summary(self):
        print("access count: {}(read:{}, write:{})".format(len(self.accesses), self.n_reads, self.n_writes))
        print("LBA: {}-{}".format(self.lba_min, self.lba_max))
        print("timestamp: {}-{}".format(format(self.accesses[0].ts, ".4f"), format(self.accesses[-1].ts, ".4f")))
        for c in self.contexts:
            print(c)
