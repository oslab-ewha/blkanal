from accbit import AccBit
from accscore import AccScore

class AccBmpCol:
    def __init__(self, lbamax, height):
        self.lbamax = lbamax
        self.height = height
        self.score = AccScore()
        self.bmp_col = []
        self.is_empty = True
        for i in range(0, height):
            self.bmp_col.append(AccBit())

    def setBitByLba(self, lba, accbit):
        idx = int((lba - 1) / float(self.lbamax) * self.height)
        self.bmp_col[idx].merge(accbit)
        self.is_empty = False
        self.score.addScore(accbit.getScore())

    def getScoreVec(self):
        return self.score.getScoreVec()

    def __str__(self):
        s = "|"
        for b in self.bmp_col:
            s += str(b)
            s += ' '
        s += "|"
        return s
