from accscore import AccScore

class AccBit:
    def __init__(self, *args):
        self.has_hit = False
        self.has_seq = False
        self.has_rnd = False
        self.has_read = False
        self.has_write = False

    def setHit(self, is_read):
        self.has_hit = True
        self.__setAccessed(is_read)

    def setSeq(self, is_read):
        self.has_seq = True
        self.__setAccessed(is_read)

    def setRnd(self, is_read):
        self.has_rnd = True
        self.__setAccessed(is_read)

    def __setAccessed(self, is_read):
        if is_read:
            self.has_read = True
        else:
            self.has_write = True

    def merge(self, accbit):
        if accbit.has_hit:
            self.has_hit = True
        if accbit.has_seq:
            self.has_seq = True
        if accbit.has_rnd:
            self.has_rnd = True
        if accbit.has_read:
            self.has_read = True
        if accbit.has_write:
            self.has_write = True
            
    def __getval(self):
        val = 0
        if self.has_read:
            val |= 1
        if self.has_write:
            val |= 2
        if self.has_hit:
            val |= 4
        if self.has_seq:
            val |= 8
        if self.has_rnd:
            val |= 16
        return val

    def getScore(self):
        score = AccScore()
        score.count = 1
        n_hits = 0
        n_seqs = 0
        n_rnds = 0
        if self.has_hit:
            n_hits += 1
        if self.has_seq:
            n_seqs += 1
        if self.has_rnd:
            n_rnds += 1
        total = float(n_hits + n_seqs + n_rnds)
        score.n_hits = n_hits / total
        score.n_seqs = n_seqs / total
        score.n_rnds = n_rnds / total
        return score

    def __str__(self):
        return format(self.__getval(), '02')
