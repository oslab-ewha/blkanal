import trace_data

class Access:
    def __init__(self, row):
        self.timestamp = float(row[0])
        if 'W' in row[4]:
            self.is_read = False
        elif 'R' in row[4]:
            self.is_read = True
        else:
            self.is_read = None
        self.lba =  int(row[5])
        self.nblks = int(row[6])

class TraceAccess(trace_data.TraceData):
    def __init__(self):
        super().__init__()
        self.accesses = []
        self.lba_max = 0

    def parseLine(self, row):
        acc = Access(row)
        if acc.is_read is None:
            return
        if acc.lba > self.lba_max:
            self.lba_max = acc.lba
        self.accesses.append(acc)
