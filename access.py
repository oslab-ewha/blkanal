class Access:
    def __init__(self, row):
        self.timestamp = float(row[0])
        if 'W' in row[4]:
            self.is_read = False
        elif 'R' in row[4]:
            self.is_read = True
        else:
            self.is_read = None
        self.ts = float(row[0])
        self.pid = int(row[2])
        self.lba =  int(row[5])
        self.nblks = int(row[6])
        self.context = None
        self.diff_lba = 0

    def setLbaDiff(self, prevs):
        if len(prevs) == 0:
            self.diff_lba = None
            return
        diff_min = None
        for prev in prevs:
            if self.isAccessedBy(prev):
                self.diff_lba = -512
                return
            diff = self.lba - (prev.lba + prev.nblks)
            if diff < 0:
                continue
            if diff_min is None or diff_min > diff:
                diff_min = diff

        if diff_min is None:
            self.diff_lba = -1024
        elif diff_min >= 1024:
            self.diff_lba = 1024
        else:
            self.diff_lba = diff_min

    def isAccessedBy(self, acc):
        last = self.lba + self.nblks - 1
        if (self.lba >= acc.lba and self.lba < acc.lba + acc.nblks) or \
           (last >= acc.lba and last < acc.lba + acc.nblks):
            return True
        return False
