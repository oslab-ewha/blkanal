import trace_data
import trace_context

class Access:
    def __init__(self, row):
        self.timestamp = float(row[0])
        if 'W' in row[4]:
            self.is_read = False
        elif 'R' in row[4]:
            self.is_read = True
        else:
            self.is_read = None
        self.pid = int(row[2])
        self.lba =  int(row[5])
        self.nblks = int(row[6])
        self.context = None

class TraceAccess(trace_data.TraceData):
    def __init__(self):
        super().__init__()
        self.accesses = []
        self.contexts = {}
        self.lba_max = 0

    def parseLine(self, row):
        acc = Access(row)
        if acc.is_read is None:
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
        self.accesses.append(acc)

    def summary(self):
        for c in self.contexts:
            print(c)
