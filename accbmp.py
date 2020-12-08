from accbmpcol import AccBmpCol
from accscore import AccScore

class AccBmp:
    def __init__(self, width, height):
        self.is_empty = True
        self.width = width
        self.height = height
        self.acc_bmp = []
        self.score = None
        self.bmpcol_forwards = []

    def append(self, bmp_col):
        if bmp_col is None:
            bmp_col = AccBmpCol(0, self.height)
        else:
            if not bmp_col.is_empty:
                self.is_empty = False

        self.acc_bmp.append(bmp_col)

    def is_valid(self):
        if self.is_empty:
            return False
        if self.acc_bmp[-1].is_empty:
            return False
        return True

    def bitmap(self):
        bmp = []
        for c in self.acc_bmp:
            bmp += c.bitmap()
        return bmp

    def calcScore(self):
        self.score = AccScore()
        for c in self.acc_bmp:
            self.score.mergeScore(c.score)
        for c in reversed(self.bmpcol_forwards):
            self.score.merge(c.score)

    def __str__(self):
        s = self.__str_bar()
        for r in reversed(range(0, self.height)):
            s += '|'
            for c in range(0, self.width):
                s += str(self.acc_bmp[c].bmp_col[r])
            s += '|'
            for c in self.bmpcol_forwards:
                s += str(c.bmp_col[r])
            s += '\n'
        s += self.__str_bar()
        return s

    def __str_bar(self):
        s = '+'
        for c in range(0, self.width):
            s += '-'
        return s + "+\n"
