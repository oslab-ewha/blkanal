class AccessHit:
    def __init__(self, ts_width):
        self.accesses = []
        self.ts_width = ts_width

    def is_hit(self, access):
        for acc in self.accesses:
            if acc.isAccessedBy(access):
                return True
        return False

    def append(self, acc):
        self.accesses.append(acc)
        if acc.ts > self.ts_width:
            ts_old = acc.ts - self.ts_width
            self.__clearOutOldAccess(ts_old)

    def __clearOutOldAccess(self, ts):
        idx = 0
        for acc in self.accesses:
            if acc.ts >= ts:
                break
            idx += 1
        self.accesses = self.accesses[idx:]
