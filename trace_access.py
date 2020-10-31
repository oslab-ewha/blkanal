import trace_data
import trace_context
import access

class TraceAccess(trace_data.TraceData):
    def __init__(self, args):
        super().__init__()
        self.accesses = []
        self.contexts = {}
        self.lba_max = 0
        self.__args = args

    def parseLine(self, row):
        acc = access.Access(row)
        if acc.ts < self.__args.ts_start or acc.ts > self.__args.ts_end:
            return
        if acc.is_read is None:
            return
        if self.__args.pidonly >= 0:
            if self.__args.pidonly != acc.pid:
                return

        if acc.lba > self.lba_max:
            self.lba_max = acc.lba

        ctx = trace_context.TraceContext(row)
        if ctx in self.contexts:
            acc.context = self.contexts[ctx]
        else:
            self.contexts[ctx] = ctx
            acc.context = ctx

        acc.context.add(acc)
        acc.setLbaDiff(self.accesses[-1 * self.__args.n_lookbacks:])
        self.accesses.append(acc)

    def summary(self):
        for c in self.contexts:
            print(c)
