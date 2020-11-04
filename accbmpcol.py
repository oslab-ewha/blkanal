from accbit import AccBit

class AccBmpCol:
    def __init__(self, lbamax, height):
        self.lbamax = lbamax
        self.height = height
        self.bmp_col = []
        self.is_empty = True
        for i in range(0, height):
            self.bmp_col.append(0)

    def setLba(self, lba, is_read, is_hit):
        idx = int((lba - 1) / float(self.lbamax) * self.height)
        self.bmp_col[idx] = AccBit(is_read, is_hit).val
        self.is_empty = False

    def getSeqScore(self, bmp_col):
        idx = 0
        n = 0
        n_seq = 0
        for c in self.bmp_col:
            if c > 0:
                n += 1
                if bmp_col.bmp_col[idx] > 0:
                    n_seq += 1
        return n_seq / float(n)

    def __str__(self):
        s = "|"
        for c in self.bmp_col:
            if c > 0:
                s += str(AccBit(c))
            else:
                s += ' '
        s += "|"
        return s
