import trace_data
import trace_context
import access
import conf

class TraceAccess(trace_data.TraceData):
    def __init__(self):
        super().__init__()
        self.accesses = []
        self.lbas_read = {}
        self.lbas_write = {}
        self.n_reads = 0
        self.n_writes = 0
        self.n_read_blks = 0
        self.n_write_blks = 0
        self.contexts = {}
        self.lba_min = -1
        self.lba_max = 0

    def load(self, path):
        if super().load(path):
            if conf.lba_start_from_1:
                self.__setbase_lba()
            return True
        return False

    def parseLine(self, row):
        acc = access.Access(row)
        if acc.lba < conf.lba_start or (conf.lba_end > 0 and acc.lba > conf.lba_end):
            return
        if acc.ts < conf.ts_start or acc.ts > conf.ts_end:
            return
        if acc.is_read is None:
            return
        if len(conf.pidonly) > 0:
            if not acc.pid in conf.pidonly:
                return
        if acc.lba == 0:
            return
        if conf.writeonly:
            if acc.is_read:
                return
        if conf.readonly:
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
        acc.setLbaDiff(self.accesses[-1 * conf.n_lookbacks:])
        self.accesses.append(acc)
        if acc.is_read:
            self.n_reads += 1
            self.n_read_blks += acc.nblks
        else:
            self.n_writes += 1
            self.n_write_blks += acc.nblks

        for i in range(acc.nblks):
            if acc.is_read:
                self.lbas_read[acc.lba + i] = True
            else:
                self.lbas_write[acc.lba + i] = True

    def __setbase_lba(self):
        for acc in self.accesses:
            acc.lba -= (self.lba_min - 1)
        self.lba_max -= (self.lba_min - 1)
        self.lba_min = 1

    def summary(self):
        print("access count: {}(read:{}, write:{})".format(len(self.accesses), self.n_reads, self.n_writes))
        lba_reads = len(self.lbas_read)
        lba_writes = len(self.lbas_write)
        print("lba count: {}(read:{}, write:{})".format(lba_reads + lba_writes, lba_reads, lba_writes))
        n_avg_read_blks = 0
        n_avg_write_blks = 0
        if self.n_reads > 0:
            n_avg_read_blks = self.n_read_blks / self.n_reads
        if self.n_writes > 0:
            n_avg_write_blks = self.n_write_blks / self.n_writes
        print("average blks: read:{}, write:{}".format(format(n_avg_read_blks, ".1f"), format(n_avg_write_blks, ".1f")))
        print("LBA: {}-{}".format(self.lba_min, self.lba_max))
        print("timestamp: {}-{}".format(format(self.accesses[0].ts, ".4f"), format(self.accesses[-1].ts, ".4f")))
        for c in self.contexts:
            print(c)
