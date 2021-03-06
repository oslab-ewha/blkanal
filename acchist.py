from accbit import AccBit

class AccessHist:
    def __init__(self, ts_width):
        self.accesses = []
        self.ts_width = ts_width

    def append(self, acc):
        if acc.ts > self.ts_width:
            ts_old = acc.ts - self.ts_width
            self.__clearOutOldAccess(ts_old)
        accbit = self.__getAccBit(acc)
        self.accesses.append(acc)
        return accbit

    def __getAccBit(self, acc):
        accbit = AccBit()
        for _acc in self.accesses:
            if _acc.isOverlappedBy(acc):
                accbit.setHit(acc.is_read)
            elif _acc.isSeqAccessedBy(acc):
                accbit.setSeq(acc.is_read)
        if not accbit.has_hit and not accbit.has_seq:
            accbit.setRnd(acc.is_read)
        return accbit

    def __clearOutOldAccess(self, ts):
        idx = 0
        for acc in self.accesses:
            if acc.ts >= ts:
                break
            idx += 1
        self.accesses = self.accesses[idx:]
