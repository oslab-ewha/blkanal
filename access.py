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
        diff_min = None
        for prev in prevs:
            diff = abs(self.lba - (prev.lba + prev.nblks))
            if diff_min is None or diff_min > diff:
                diff_min = diff

        self.diff_lba = diff_min
